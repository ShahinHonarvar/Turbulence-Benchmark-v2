def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

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
        for i in range(length):
            left = int(s[i:length])
            right = int(s[0:length - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result