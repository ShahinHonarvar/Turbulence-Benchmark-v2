def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    x = numbers[803]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result