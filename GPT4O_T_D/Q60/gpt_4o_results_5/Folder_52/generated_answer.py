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

    def is_truncatable_left_right(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        length = len(str_n)
        for i in range(length):
            left = int(str_n[i:])
            right = int(str_n[:length - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    x = numbers[52]
    result = []
    for num in range(10, x + 1):
        if is_truncatable_left_right(num):
            result.append(num)
    return sorted(result, reverse=True)