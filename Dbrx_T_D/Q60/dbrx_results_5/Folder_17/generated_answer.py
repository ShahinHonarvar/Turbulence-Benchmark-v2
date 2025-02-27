from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[36]
    result = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        truncatable = True
        while num > 10:
            if not isprime(num) or num % 10 == 0 or num < 10:
                truncatable = False
                break
            num = int(str(num)[1:]) if num < 100 else int(str(num)[:-1])
        if truncatable:
            result.append(num)
    result.sort(reverse=True)
    return result