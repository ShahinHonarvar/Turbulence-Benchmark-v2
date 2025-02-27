def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and (not is_prime(num)):
        return False
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[:i])) or int(str(num)[:i]) == 0:
            return False
    return True

def all_left_truncatable_prime(limit):
    primes = [2, 3, 5, 7]
    current_prime = 2
    while current_prime < limit:
        if left_truncatable_prime(current_prime):
            primes.append(current_prime)
        current_prime += 1
    return sorted(primes)