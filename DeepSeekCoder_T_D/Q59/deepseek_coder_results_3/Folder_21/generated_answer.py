def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []

    def check(num):
        while num > 0:
            if num not in primes:
                return False
            num //= 10
        return True
    queue = [2, 3, 5, 7]
    while queue:
        current = queue.pop(0)
        if current >= limit:
            continue
        if is_prime(current):
            primes.append(current)
            for digit in [1, 3, 7, 9]:
                new_prime = current * 10 + digit
                if new_prime < limit and is_prime(new_prime) and check(new_prime):
                    queue.append(new_prime)
    return sorted(primes)

def all_left_truncatable_prime(tup):
    x = tup[175]
    return left_truncatable_primes(x)