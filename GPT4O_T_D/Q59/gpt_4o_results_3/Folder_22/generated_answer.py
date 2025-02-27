def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        temp = n
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    x = numbers[85]
    left_truncatable_primes = []
    for number in range(2, x):
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return left_truncatable_primes