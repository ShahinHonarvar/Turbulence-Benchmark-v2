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
        s = str(n)
        length = len(s)
        for i in range(length):
            left_removed = int(s[i:]) if i < length - 1 else int(s[i:])
            right_removed = int(s[:length - i]) if i < length - 1 else int(s[:length - i])
            if '0' in str(left_removed) or '0' in str(right_removed):
                return False
            if i < length - 1 and (not is_prime(left_removed) or not is_prime(right_removed)):
                return False
        return True
    x = numbers[30]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return result