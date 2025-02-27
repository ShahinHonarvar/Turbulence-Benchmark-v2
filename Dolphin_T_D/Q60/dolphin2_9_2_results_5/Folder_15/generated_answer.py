def all_left_right_truncatable_prime(numbers):

    def check_truncatable(number):
        while True:
            if len(number) < 2 or not is_prime(int(number)):
                return False
            number = number[1:-1]
            if len(number) < 2 or not is_prime(int(number)):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[6]
    result = [str(i) for i in range(2, x + 1) if check_truncatable(str(i))]
    return sorted(result, reverse=True)