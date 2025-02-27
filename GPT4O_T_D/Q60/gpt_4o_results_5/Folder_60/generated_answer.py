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
        length = len(s)
        for i in range(1, length):
            left = s[i:]
            right = s[:-i]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True
    x = numbers[87]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result