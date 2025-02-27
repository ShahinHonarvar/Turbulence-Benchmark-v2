def all_right_truncatable_prime(numtuple):
    x = numtuple[55]
    rtp = set()
    for i in range(2, x):
        if isprime(i):
            for j in range(1, len(str(i))):
                ik = int(str(i)[:-j])
                if isprime(ik):
                    rtp.add(ik)
    return sorted(rtp, reverse=True)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True