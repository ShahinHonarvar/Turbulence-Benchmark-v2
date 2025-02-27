def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if str(n).count('0') > 0:
            return False
        while len(str(n)) > 1:
            if str(n).count('0') > 0:
                return False
            if not is_prime(n):
                return False
            n = n // 10
            if n == 0:
                n = int(str(n).replace('0', ''))
            if n == 0:
                n = int(str(n)[::-1].replace('0', ''))
        return True
    x = numbers[26]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result)