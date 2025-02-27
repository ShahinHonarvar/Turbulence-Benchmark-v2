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

def all_left_right_truncatable_prime(numbers):
    num = numbers[41]

    def is_left_right_truncatable(y):
        if y == 1 or y == 2 or y % 10 == 0:
            return False
        str_y = str(y)
        left = str_y[1:-1]
        right = str_y[:-1]
        while len(left) % 2 != 0 and len(right) == len(str_y) - 2:
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
            left = left[1:-1]
            right = right[:-1]
        if not is_prime(int(right)) or not is_prime(int(left)):
            return False
        return True
    return sorted([i for i in range(1, num + 1) if is_left_right_truncatable(i)], reverse=True)