def all_left_right_truncatable_prime(numbers):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_truncatable_prime(number):
        str_num = str(number)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    x = numbers[23]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes