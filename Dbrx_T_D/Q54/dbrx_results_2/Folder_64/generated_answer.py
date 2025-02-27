from sympy import isprime

def all_right_truncatable_prime(x):
    rtp = []
    for i in range(1, 10):
        if isprime(i):
            rtp.append(i)
    for j in range(10, x):
        num = j
        while num > 0:
            if not isprime(num):
                break
            num = num // 10
        else:
            rtp.append(j)
    return sorted(list(set(rtp)))