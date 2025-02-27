def all_left_truncatable_prime(lst):

    def is_prime(n):
        if n <= 1:
            return True
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = lst[87]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and all([is_prime(i // 10 ** j) for j in range(1, len(str(i)))]):
            left_truncatable_primes.append(i)
    return left_truncatable_primes