def all_left_truncatable_prime(tuple_input):

    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        for i in range(len(str(n)) - 1, 0, -1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = tuple_input[945]
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(left_truncatable_primes, reverse=True)