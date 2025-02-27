from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[7]
    rtp = []
    for i in range(1, x):
        j = 10 ** len(str(i))
        while j > 0:
            if isprime(i):
                rtp.append(i)
            else:
                break
            i = i % (j // 10)
            j //= 10
    return sorted(rtp)