from sympy import isprime

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[81]
    rtp = []
    for i in range(1, x):
        if isprime(i):
            is_rtp = True
            while i > 1:
                if not isprime(int(str(i)[1:])):
                    is_rtp = False
                    break
                i = int(str(i)[:-1])
            if is_rtp:
                rtp.append(i)
    return sorted(rtp, reverse=True)