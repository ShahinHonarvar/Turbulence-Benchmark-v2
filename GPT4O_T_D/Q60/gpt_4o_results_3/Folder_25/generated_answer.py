def all_left_right_truncatable_prime(numbers):
    x = numbers[92]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 2:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return is_prime(int(s))
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result)