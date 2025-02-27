def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))
    x = numbers[39]
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and '0' not in str(i) and left_truncatable(i)]
    return sorted(left_truncatable_primes)