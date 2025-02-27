def all_right_truncatable_prime(numbers):
    x = numbers[26]
    primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(2, x):
        truncated_num = num
        while truncated_num:
            if not is_prime(truncated_num):
                break
            truncated_num //= 10
        else:
            primes.append(num)
    return sorted(primes)