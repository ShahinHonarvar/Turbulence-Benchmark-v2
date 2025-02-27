def all_left_truncatable_prime(numbers):
    x = numbers[32]

    def is_left_truncatable_prime(n):
        if n < 10:
            return n in {2, 3, 5, 7}
        if '0' in str(n) or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return all((is_left_truncatable_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])