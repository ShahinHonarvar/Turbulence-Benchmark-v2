def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    primes = []
    x = t[630]
    for num in range(x):
        if is_prime(num):
            truncation = num
            while truncation > 0:
                if not is_prime(int(truncation)):
                    break
                truncation = int(str(truncation)[1:])
            else:
                primes.append(num)
    return sorted(primes, reverse=True)