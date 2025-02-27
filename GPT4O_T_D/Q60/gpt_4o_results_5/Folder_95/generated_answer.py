def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        length = len(str_prime)
        for i in range(length):
            left_truncate = int(str_prime[i:])
            right_truncate = int(str_prime[:length - i])
            if not (is_prime(left_truncate) and is_prime(right_truncate)):
                return False
        return True
    x = numbers[77]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result