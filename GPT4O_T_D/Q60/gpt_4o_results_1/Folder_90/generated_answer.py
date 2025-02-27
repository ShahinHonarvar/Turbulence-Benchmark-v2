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
        converted = str(n)
        for i in range(len(converted)):
            if not is_prime(int(converted[i:])) or not is_prime(int(converted[:len(converted) - i])):
                return False
        return True
    if len(numbers) <= 466:
        return []
    x = numbers[466]
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)