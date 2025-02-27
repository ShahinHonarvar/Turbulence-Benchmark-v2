from sympy import isprime

def trailing_digit(num):
    return int(str(num)[-1])

def all_right_truncatable_prime(tup):
    x = tup[57]
    result = []
    for num in range(x - 1, 0, -1):
        if isprime(num) and set(str(num)).issuperset({2, 3, 5, 7}):
            factor = trailing_digit(num)
            while factor != 0:
                if int(str(num)[:-1]) % factor != 0:
                    break
                num = int(str(num)[:-1])
                factor = trailing_digit(num)
            else:
                result.append(num)
    return sorted(result, reverse=True) if result else []