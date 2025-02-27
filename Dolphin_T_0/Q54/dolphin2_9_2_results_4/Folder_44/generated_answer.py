def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[39]
    result = []
    for num in range(2, x):
        if is_prime(num):
            one_digit_removed = num // 10
            while one_digit_removed > 0:
                if not is_prime(one_digit_removed):
                    break
                one_digit_removed //= 10
            else:
                result.append(num)
    return sorted(result)