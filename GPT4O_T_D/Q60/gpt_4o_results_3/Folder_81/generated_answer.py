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

    def all_truncations_prime(n):
        s = str(n)
        while len(s) > 2:
            s = s[1:-1]
            if not is_prime(int(s)):
                return False
        return True

    def is_truncatable_prime(n):
        return is_prime(n) and all_truncations_prime(n)
    x = numbers[98]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_truncatable_prime(num):
            result.append(num)
    return result