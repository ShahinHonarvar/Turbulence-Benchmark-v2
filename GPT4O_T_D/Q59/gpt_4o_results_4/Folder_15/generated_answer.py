def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    x = numbers[6]
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)], reverse=True)