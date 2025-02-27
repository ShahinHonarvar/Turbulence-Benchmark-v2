def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True
    x = numbers[87]
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes)