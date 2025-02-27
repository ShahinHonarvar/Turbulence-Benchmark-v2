def all_left_right_truncatable_prime(numbers):

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
        if '0' in str_prime:
            return False
        length = len(str_prime)
        for i in range(1, length):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:length - i])):
                return False
        return True
    x = numbers[85]
    left_right_truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)