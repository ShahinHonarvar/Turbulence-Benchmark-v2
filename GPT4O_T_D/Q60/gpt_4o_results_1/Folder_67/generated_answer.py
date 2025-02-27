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

    def is_no_zero_prime(n):
        return '0' not in str(n) and is_prime(n)

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not is_no_zero_prime(int(s)):
                return False
        return True
    result = []
    if len(numbers) > 71:
        x = numbers[71]
        for num in range(x + 1):
            if is_no_zero_prime(num) and is_left_right_truncatable_prime(num):
                result.append(num)
    return sorted(result, reverse=True)