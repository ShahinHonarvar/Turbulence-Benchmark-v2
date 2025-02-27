def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:length - i])):
                return False
        return True
    result = [i for i in range(10, x + 1) if is_lr_truncatable_prime(i)]
    return sorted(result, reverse=True)