def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num, primes):
    if num in primes:
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])):
                return False
        return True
    return False

def all_left_truncatable_prime(limit):
    primes = [2, 3, 5, 7]
    current_num = 0
    while len(primes) < 26:
        current_num += 1
        if left_truncatable_prime(current_num, primes):
            primes.append(current_num)
    return sorted(primes)