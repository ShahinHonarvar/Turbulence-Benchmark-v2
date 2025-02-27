from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[792]
    rtp = []
    for num in range(1, x):
        while num > 0:
            if isprime(num) and num < x:
                rtp.append(num)
                break
            num = int(str(num)[:-1])
    return sorted(list(set(rtp)))