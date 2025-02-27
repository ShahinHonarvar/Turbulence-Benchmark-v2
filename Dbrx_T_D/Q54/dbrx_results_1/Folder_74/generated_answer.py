def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_right_truncatable_primes(n):
    rtp = []
    for i in range(1, 10):
        if is_prime(i):
            rtp.append(i)
    for j in range(1, n):
        temp = []
        for k in rtp:
            for i in range(1, 10):
                if is_prime(int(str(k) + str(i))):
                    temp.append(int(str(k) + str(i)))
        rtp = temp
    return rtp

def all_right_truncatable_prime(t):
    x = t[36]
    rtp = generate_right_truncatable_primes(x)
    result = [i for i in rtp if i < x]
    return sorted(result)