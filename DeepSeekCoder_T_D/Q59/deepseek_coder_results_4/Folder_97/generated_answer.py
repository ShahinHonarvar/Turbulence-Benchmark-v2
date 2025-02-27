def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []
    queue = [2, 3, 5, 7]
    while queue:
        current = queue.pop(0)
        if current < limit and is_prime(current):
            primes.append(current)
            for digit in range(1, 10):
                next_num = int(str(digit) + str(current))
                if is_prime(next_num):
                    queue.append(next_num)
    return sorted(primes)

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    return left_truncatable_primes(x)