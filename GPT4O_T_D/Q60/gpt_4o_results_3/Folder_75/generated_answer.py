def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s)) or not is_prime(int(s[::-1])):
                return False
            s = s[1:-1]
        return is_prime(n)
    if len(numbers) <= 41:
        return []
    x = numbers[41]
    result = []
    for number in range(10, x + 1):
        if is_truncatable_prime(number):
            result.append(number)
    return sorted(result)