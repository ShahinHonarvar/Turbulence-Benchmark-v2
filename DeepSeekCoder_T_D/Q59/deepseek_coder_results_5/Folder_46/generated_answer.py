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
        num = queue.pop(0)
        if num < limit and is_prime(num):
            primes.append(num)
            for digit in range(1, 10):
                new_num = int(str(digit) + str(num))
                if is_prime(new_num):
                    queue.append(new_num)
    return sorted(primes)

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    return left_truncatable_primes(x)