def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        while len(str_num) > 2:
            str_num = str_num[1:-1]
            if not is_prime(int(str_num)):
                return False
        return True
    x = numbers[10]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)