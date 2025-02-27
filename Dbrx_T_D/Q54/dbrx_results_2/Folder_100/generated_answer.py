from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[26]
    rtp = []
    for i in range(1, int(x)):
        if isprime(i):
            is_rtp = True
            while i > 0:
                if not isprime(i):
                    is_rtp = False
                    break
                i = int(str(i)[:-1])
            if is_rtp:
                rtp.append(i)
    return sorted(rtp)