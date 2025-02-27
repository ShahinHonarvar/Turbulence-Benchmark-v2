def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            for i in range(len(num_str), 0, -1):
                if not is_prime(int(num_str[:i])):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)