def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[22]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        current = num
        is_truncatable_prime = True
        while current > 0:
            if not is_prime(current):
                is_truncatable_prime = False
                break
            current //= 10
        if is_truncatable_prime and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)