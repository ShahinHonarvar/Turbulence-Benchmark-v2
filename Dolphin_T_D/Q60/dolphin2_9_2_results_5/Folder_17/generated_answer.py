def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[36]
    result = [i for i in range(x, 1, -1) if is_prime(i)]
    result = [i for i in result if set(str(i)).issubset('123456789')]
    return [i for i in result if is_prime(i) and is_prime(int(str(i).pop())) and is_prime(int(str(i).pop(0)))]