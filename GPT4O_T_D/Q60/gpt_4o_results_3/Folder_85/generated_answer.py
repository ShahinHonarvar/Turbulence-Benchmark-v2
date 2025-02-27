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

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            left_truncate = int(str_n[i:]) if i < len(str_n) else None
            right_truncate = int(str_n[:len(str_n) - i]) if i < len(str_n) else None
            if left_truncate and (not is_prime(left_truncate)):
                return False
            if right_truncate and (not is_prime(right_truncate)):
                return False
        return True
    if len(numbers) <= 94:
        return []
    x = numbers[94]
    result = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)