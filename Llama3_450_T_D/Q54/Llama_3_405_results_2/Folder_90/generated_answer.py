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

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    x = numbers[466]
    right_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable_prime(i)]
    return sorted(right_truncatable_primes, reverse=True)