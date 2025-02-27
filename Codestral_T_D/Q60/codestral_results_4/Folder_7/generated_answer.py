def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        for i in range(1, len(num_str)):
            if num_str[i] == '0':
                return False
            if not is_prime(int(num_str[i:])):
                return False
        return True

    def is_right_truncatable_prime(n):
        num_str = str(n)
        for i in range(1, len(num_str)):
            if num_str[-i] == '0':
                return False
            if not is_prime(int(num_str[:-i])):
                return False
        return True
    x = numbers[803]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)