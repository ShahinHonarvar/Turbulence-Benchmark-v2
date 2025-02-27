def all_left_truncatable_prime(t):
    x = t[36]

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return False
        while n > 1:
            if n % 10 == 0:
                return False
            n //= 10
        return True
    primes = [2]
    left_truncatable_primes = []
    current_number = 3
    while current_number < x:
        if is_left_truncatable(current_number) and is_prime(current_number):
            left_truncatable_primes.append(current_number)
        if is_prime(current_number):
            primes.append(current_number)
        current_number += 1
    return sorted(left_truncatable_primes + primes)