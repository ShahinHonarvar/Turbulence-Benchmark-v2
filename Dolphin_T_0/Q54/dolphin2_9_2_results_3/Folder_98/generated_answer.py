def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    numbers = list(numbers)
    numbers.sort(reverse=True)
    x = numbers[8]
    result = [n for n in numbers if is_right_truncatable(n) and n < x]
    return result