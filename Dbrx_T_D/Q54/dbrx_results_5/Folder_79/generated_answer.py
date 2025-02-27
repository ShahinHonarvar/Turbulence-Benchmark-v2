from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[91]
    rtp = []
    for i in range(1, 10):
        if isprime(i):
            rtp.append(i)
    for i in rtp:
        for j in range(2, len(str(i))):
            if isprime(int(str(i)[:-j])) is False:
                rtp.remove(i)
                break
    rtp = [num for num in rtp if num < x]
    return sorted(rtp)