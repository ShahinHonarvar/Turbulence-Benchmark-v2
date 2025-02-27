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

    def is_truncatable_prime(p):
        str_p = str(p)
        if '0' in str_p:
            return False
        for i in range(1, len(str_p)):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:i])):
                return False
        return True
    if len(numbers) <= 69:
        return []
    x = numbers[69]
    result = []
    for num in range(11, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)