def all_left_right_truncatable_prime(numbers):
    x = numbers[8]

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
        if '0' in s:
            return False
        length = len(s)
        for i in range(1, length):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:length - i])):
                return False
        return is_prime(n)
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)