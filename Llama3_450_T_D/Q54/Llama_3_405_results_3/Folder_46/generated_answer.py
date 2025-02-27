def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    x = numbers[33]
    return sorted([i for i in range(2, x) if is_prime(i) and right_truncatable_prime(i)])