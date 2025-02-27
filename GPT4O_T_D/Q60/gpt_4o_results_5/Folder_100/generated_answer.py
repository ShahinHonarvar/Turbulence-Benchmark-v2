def all_left_right_truncatable_prime(numbers):
    x = numbers[26]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        length = len(s)
        if '0' in s:
            return False
        for i in range(length):
            if not is_prime(int(s[i:length - i])) or not is_prime(int(s[i:]) if length - i > 0 else 0):
                return False
        return True
    result = []
    for number in range(2, x + 1):
        if is_truncatable_prime(number):
            result.append(number)
    return result