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
        for i in range(1, len(str_prime)):
            left_trunc = int(str_prime[i:])
            right_trunc = int(str_prime[:len(str_prime) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    x = numbers[100]
    truncatable_primes = []
    for number in range(2, x + 1):
        if '0' in str(number):
            continue
        if is_prime(number) and is_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes