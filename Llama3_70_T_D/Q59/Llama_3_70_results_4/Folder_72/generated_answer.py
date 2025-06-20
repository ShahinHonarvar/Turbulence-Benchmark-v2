def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[31]

    def is_left_truncatable_prime(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)