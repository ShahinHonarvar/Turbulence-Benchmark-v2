def all_right_truncatable_prime(numbers):
    x = numbers[24]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_right_truncatable = True
            for i in range(len(str_num)):
                if not is_prime(int(str_num[:-i - 1])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(num)
    return sorted(primes)