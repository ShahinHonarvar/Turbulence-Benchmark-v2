def all_right_truncatable_prime(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(number):
        if number <= 1:
            return False
        while number > 1:
            if not is_prime(number):
                return False
            number = number // 10
        return True
    numbers = list(numbers)
    numbers.sort()
    last_digit = numbers[-1]
    if last_digit == 0:
        numbers.pop()
    return [i for i in numbers if is_right_truncatable_prime(i)]