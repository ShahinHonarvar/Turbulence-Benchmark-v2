from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[85]
    result = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            flag = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    flag = False
                    break
            if flag:
                result.append(num)
    return sorted(result)