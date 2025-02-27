def all_left_right_truncatable_prime(numbers):
    x = numbers[46]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable(prime):
        str_prime = str(prime)
        while len(str_prime) > 2:
            str_prime = str_prime[1:-1]
            if '0' in str_prime or not is_prime(int(str_prime)):
                return False
        return is_prime(int(str_prime))
    truncatable_primes = []
    for num in range(23, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)