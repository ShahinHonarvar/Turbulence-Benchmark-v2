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
            for digit in [1, 2, 3, 5, 7, 9]:
                new_num = current * 10 + digit
                if is_prime(new_num) and check(new_num):
                    queue.append(new_num)
    return sorted(primes)

def all_left_truncatable_prime(numbers):
    x = numbers[98]
    return left_truncatable_primes(x)