def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncate(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            left_truncated = int(str_prime[i:])
            right_truncated = int(str_prime[:-i])
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                return False
        return True
    x = numbers[70]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and left_right_truncate(num):
            result.append(num)
    return sorted(result, reverse=True)