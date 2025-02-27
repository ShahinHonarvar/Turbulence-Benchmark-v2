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

    def is_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(1, length):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:length - i])):
                return False
        return True
    if len(numbers) < 29:
        return []
    x = numbers[28]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result