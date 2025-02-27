def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []
    queue = [str(i) for i in range(1, 10) if is_prime(i)]
    while queue:
        current = queue.pop(0)
        current_num = int(current)
        if current_num < limit:
            primes.append(current_num)
            for digit in '123456789':
                new_num = int(digit + current)
                if is_prime(new_num):
                    queue.append(str(new_num))
    return sorted(primes)

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    return left_truncatable_primes(x)