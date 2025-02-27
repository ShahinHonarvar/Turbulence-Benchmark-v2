import sympy

def all_left_truncatable_prime(x):
    prime = sympy.isprime
    result = []
    for i in range(5, x):
        if prime(i):
            str_i = str(i)
            if '0' in str_i:
                continue
            a = int(str_i[:len(str_i) - 1])
            while a not in [0, 1, 2, 4, 5, 6, 8, 9] and a > 2 and prime(a):
                str_a = str(a)
                if '0' in str_a:
                    break
                a = int(str_a[:len(str_a) - 1])
            if a == 2 or (a == a // 2 and a % 2 == 0):
                result.append(i)
    return sorted(result)