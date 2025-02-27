from math import sqrt

def all_left_truncatable_prime(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def is_left_truncatable_prime(number):
        if '0' in str(number):
            return False
        for i in range(1, len(str(number))):
            if not is_prime(int(str(number)[:i])):
                return False
        return True
    result = [number for number in numbers if is_left_truncatable_prime(number) and is_prime(number)]
    result.sort(reverse=True)
    return result