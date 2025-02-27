def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left_right(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            truncated_str = num_str[i:]
            if not is_prime(int(truncated_str)):
                return False
            truncated_str = num_str[:len(num_str) - i]
            if not is_prime(int(truncated_str)):
                return False
        return True
    x = numbers[38]
    result = [i for i in range(10, x + 1) if is_prime(i) and truncate_left_right(i)]
    return sorted(result, reverse=True)