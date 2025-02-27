def all_left_right_truncatable_prime(integers):
    x = integers[61]

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

    def left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(1, length):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:i]))):
                return False
        return True
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and left_right_truncatable(num):
            result.append(num)
    return sorted(result)