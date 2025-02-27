def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    if len(numbers) <= 50:
        return []
    x = numbers[50]
    left_truncatable_primes = []
    for num in range(x):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)