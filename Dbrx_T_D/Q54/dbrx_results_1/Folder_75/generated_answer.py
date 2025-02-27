def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def generate_right_truncatable_primes(limit):
    rtp = []
    for num in range(1, limit):
        if is_prime(num):
            rtp.append(num)
            while True:
                num = 10 * num + 1
                if num >= limit:
                    break
                if not is_prime(num):
                    break
                rtp.append(num)
    return rtp

def all_right_truncatable_prime(t):
    x = t[41]
    rtp = generate_right_truncatable_primes(x)
    return sorted(list(set(rtp)))