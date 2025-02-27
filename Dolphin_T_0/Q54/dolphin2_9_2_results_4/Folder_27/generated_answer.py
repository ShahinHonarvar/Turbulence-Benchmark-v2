def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    primes = []
    for num in range(x):
        if is_prime(num):
            truncated = num
            while truncated > 0:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)