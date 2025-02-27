def all_left_right_truncatable_prime(val):

    def check_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def left_truncatable(number):
        while number >= 10:
            number = number // 10
            if not check_prime(number):
                return False
        if check_prime(number):
            return True
        return False

    def right_truncatable(number):
        original_number = number
        while number >= 10:
            number = int(str(number)[:-1])
            if not check_prime(number):
                return False
        if original_number // 10 > 1 and check_prime(number):
            return True
        return False
    result = []
    for num in range(val):
        if check_prime(num) and left_truncatable(num) and right_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result