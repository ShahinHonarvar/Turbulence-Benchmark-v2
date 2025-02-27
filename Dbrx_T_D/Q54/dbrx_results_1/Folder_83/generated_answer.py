from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    rtp = []
    for i in range(1, 10):
        if isprime(i):
            rtp.append(i)
    for i in range(10, x):
        if isprime(i):
            is_rtp = True
            j = i
            while j > 0:
                if not isprime(j):
                    is_rtp = False
                    break
                j = j // 10
            if is_rtp:
                rtp.append(i)
    return sorted(rtp)