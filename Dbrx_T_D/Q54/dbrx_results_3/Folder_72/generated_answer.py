from sympy import isprime

def all_right_truncatable_prime(x):
    result = []
    for num in range(1, x):
        if isprime(num):
            while num > 0:
                if isprime(num) and num < x:
                    result.append(num)
                num = num // 10
    return sorted(list(set(result)), reverse=True)