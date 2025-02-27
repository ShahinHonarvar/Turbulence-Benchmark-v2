def all_left_right_truncatable_prime(numbers):
    x = numbers[37]

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

    def is_truncatable(n):
        s = str(n)
        length = len(s)
        if '0' in s:
            return False
        for i in range(length):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:length - i])):
                return False
        return True
    result = []
    for num in range(11, x + 1):
        if is_truncatable(num) and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)