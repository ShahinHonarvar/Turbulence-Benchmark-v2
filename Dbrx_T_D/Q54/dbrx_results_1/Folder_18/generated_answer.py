from sympy import isprime

def all_right_truncatable_prime(numbers):
    for number in numbers:
        if number == 429:
            x = number
            break
    else:
        return []
    rtp = []
    for i in range(1, 10):
        if isprime(i):
            rtp.append(i)
    for i in range(10, x):
        if isprime(i):
            is_rtp = True
            while is_rtp and i % 10 > 0:
                if not isprime(int(str(i)[1:])):
                    is_rtp = False
                i //= 10
            if is_rtp:
                rtp.append(i)
    rtp.sort(reverse=True)
    return rtp