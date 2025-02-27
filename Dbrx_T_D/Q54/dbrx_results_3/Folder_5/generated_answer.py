from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[55]
    rtp = []
    for num in range(1, x):
        if isprime(num):
            while num > 0:
                if not isprime(num):
                    break
                num = num // 10
            else:
                rtp.append(num)
    return sorted(rtp)