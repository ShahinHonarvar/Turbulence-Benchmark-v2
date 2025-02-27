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
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:length - i])):
                return False
        return True
    if len(numbers) <= 65:
        return []
    x = numbers[65]
    result = []
    for num in range(11, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)