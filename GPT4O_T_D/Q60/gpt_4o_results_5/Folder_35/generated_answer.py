def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 177:
        return []
    x = numbers[177]

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
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    result = []
    for number in range(10, x + 1):
        if '0' not in str(number) and is_prime(number) and left_right_truncatable(number):
            result.append(number)
    return result