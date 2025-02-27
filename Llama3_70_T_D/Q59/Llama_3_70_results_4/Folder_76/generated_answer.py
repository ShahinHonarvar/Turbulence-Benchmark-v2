def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = numbers[370]
    left_truncatable_primes = []
    for num in range(x - 1, 0, -1):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes