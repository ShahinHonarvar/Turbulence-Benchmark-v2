def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes)