from sympy import isprime
    from itertools import product

def all_left_right_truncatable_prime(tup):
    x = tup[760]
    result = []
    for digits in range(1, len(str(x)) + 1):
        for num in (int(''.join(p)) for p in product('123456789', repeat=digits)):
            if isprime(num) and (not '0' in str(num)):
                dir = 0
                while num > 10:
                    if dir > 1 or not isprime(num):
                        break
                    num = int(str(num)[1:])
                    num1 = int(str(num)[:-1])
                    dir += 1
                if num > 10 and dir > 1 and isprime(num):
                    result.append(num)
    return sorted(result, reverse=True)