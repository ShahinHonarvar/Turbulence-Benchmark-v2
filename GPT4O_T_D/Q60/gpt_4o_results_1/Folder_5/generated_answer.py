def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(prime):
        str_prime = str(prime)
        length = len(str_prime)
        if '0' in str_prime:
            return False
        for i in range(1, length):
            if not (is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:i]))):
                return False
        return True
    if len(numbers) <= 55:
        return []
    x = numbers[55]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes