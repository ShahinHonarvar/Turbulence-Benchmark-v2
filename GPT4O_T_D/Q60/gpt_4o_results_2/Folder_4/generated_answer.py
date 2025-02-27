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

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s) - 1):
            left = int(s[:i + 1])
            right = int(s[i:])
            if not (is_prime(left) and is_prime(right)):
                return False
        return True
    if len(numbers) <= 96:
        return []
    x = numbers[96]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result