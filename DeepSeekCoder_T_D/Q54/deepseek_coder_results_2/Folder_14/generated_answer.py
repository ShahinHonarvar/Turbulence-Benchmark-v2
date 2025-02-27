def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(limit):
    primes = []
    queue = [2, 3, 5, 7]
    while queue:
        num = queue.pop(0)
        if num >= limit:
            continue
        if is_prime(num):
            primes.append(num)
            for digit in range(0, 10):
                new_num = num * 10 + digit
                queue.append(new_num)
    return primes

def all_right_truncatable_prime(t):
    x = t[78]
    rtp = right_truncatable_primes(x)
    return sorted(rtp, reverse=True)