from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[784]
    rtp = []
    for num in range(1, x):
        while num > 0:
            if isprime(num):
                rtp.append(num)
            num = num // 10
    return sorted(list(set(rtp)))