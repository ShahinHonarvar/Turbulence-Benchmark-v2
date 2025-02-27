def all_left_right_truncatable_prime(numbers):
    x = numbers[78]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                return False
        return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes