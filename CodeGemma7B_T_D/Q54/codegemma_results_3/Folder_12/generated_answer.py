def all_right_truncatable_prime(numbers):
    x = numbers[70]
    right_truncatable_primes = []
    for num in reversed(numbers):
        if is_prime(num):
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[:-i])):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True