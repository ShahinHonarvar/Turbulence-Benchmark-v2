def all_left_right_truncatable_prime(x):

    def is_truncatable_prime(n):
        return all((int(str(n)[i:j]) in prime_set for i in range(len(str(n))) for j in range(i + 1, len(str(n)) + 1)))
    prime_set = set()
    for i in range(2, int(x ** 0.5) + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            prime_set.add(i)
    return sorted(list(filter(is_truncatable_prime, range(2, x))), reverse=True)