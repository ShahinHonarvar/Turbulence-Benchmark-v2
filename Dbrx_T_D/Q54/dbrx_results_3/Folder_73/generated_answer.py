from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    rtp = []
    for i in range(2, x):
        if isprime(i):
            while i < x:
                if isprime(i) and i not in rtp:
                    rtp.append(i)
                i *= 10
    return sorted(rtp)