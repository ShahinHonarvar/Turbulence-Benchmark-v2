def all_right_truncatable_prime(num_tuple):

    def is_right_truncatable_prime(n):
        without = [int(str(n)[i:j]) for i in range(1, len(str(n))) for j in range(i, len(str(n)) + 1)]
        return all((is_prime(x) for x in without))

    def is_prime(n):
        return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

    def get_right_truncatable_primes(n):
        return [n for n in range(n - 1, 1, -1) if is_right_truncatable_prime(n)]
    x = num_tuple[-1]
    right_truncatable_primes = get_right_truncatable_primes(x)
    return sorted([*set(right_truncatable_primes)], reverse=True) if len(right_truncatable_primes) != 0 else []