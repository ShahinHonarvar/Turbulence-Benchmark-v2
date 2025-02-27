def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def truncate_left_right_prime(n):
        digits = str(n)
        if '0' in digits:
            return False
        length = len(digits)
        for i in range(length):
            left_truncated = int(digits[i:length])
            right_truncated = int(digits[0:length - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    x = numbers[126]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and truncate_left_right_prime(num):
            result.append(num)
    return sorted(result, reverse=True)