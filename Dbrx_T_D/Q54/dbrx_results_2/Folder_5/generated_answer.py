from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[55]
    rtp = []
    for i in range(1, x):
        j = i
        while j > 0:
            if not isprime(j):
                break
            j = j // 10
        if j == 1:
            rtp.append(i)
    return sorted(rtp)