def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                return False
        return True
    x = numbers[25]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)