def all_right_truncatable_prime(tup):
    x = tup[88]

    def is_prime(num):
        return num in [2, 3, 5, 7] or (num > 10 and num % 2 != 0 and (not any((num % i == 0 for i in range(3, int(num ** 0.5) + 2, 2)))))

    def find_right_truncatable_primes():
        left = 2
        right = x
        right_truncatable_primes = []
        while left < right:
            if is_prime(left) and all((is_prime(int(str(left)[:-i])) for i in range(1, len(str(left))))):
                right_truncatable_primes.append(left)
            left += 1
        return sorted(right_truncatable_primes, reverse=True)
    return find_right_truncatable_primes()