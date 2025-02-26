def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[74]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            current = num
            is_truncatable = True
            while current > 9:
                current //= 10
                if not is_prime(current):
                    is_truncatable = False
                    break
            if is_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)