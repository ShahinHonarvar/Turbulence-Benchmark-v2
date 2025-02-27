def all_right_truncatable_prime(numbers):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_right_truncatable_prime(number):
        if not is_prime(number):
            return False
        str_number = str(number)
        for i in range(len(str_number) - 1, 0, -1):
            if not is_prime(int(str_number[:i])):
                return False
        return True
    x = numbers[52]
    return sorted([i for i in range(x, 0, -1) if is_right_truncatable_prime(i)], reverse=False)