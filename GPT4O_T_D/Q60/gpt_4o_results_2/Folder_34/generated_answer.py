def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s:
                break
            if '0' in s or not is_prime(int(s)):
                return False
        return True
    x = numbers[18]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)