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
        s = str(n)
        while len(s) > 1:
            if '0' in s:
                return False
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    if len(numbers) <= 49:
        raise ValueError('The tuple should contain at least 50 integers')
    x = numbers[49]
    result = []
    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result)