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

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[:length - i])) or not is_prime(int(s[i:])):
                return False
        return True
    if len(numbers) <= 55:
        return []
    x = numbers[55]
    result = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return result