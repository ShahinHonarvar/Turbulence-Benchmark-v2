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
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            left = int(s[i:])
            right = int(s[:length - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    x = numbers[975]
    result = []
    for number in range(2, x + 1):
        if is_left_right_truncatable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result