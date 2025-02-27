def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:-i - 1])):
                return False
        return True
    x = numbers[55]
    right_truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes)