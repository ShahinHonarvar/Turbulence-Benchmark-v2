def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_left_truncatable_primes():
    primes = [1, 3, 7]
    for x in primes:
        for i in range(1, 10):
            num = x * 10 + i
            if is_prime(num):
                primes.append(num)
    return primes

def all_left_truncatable_prime(high):
    return [x for x in generate_left_truncatable_primes() if x < high]