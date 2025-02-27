def all_right_truncatable_prime(a_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = a_tuple[87]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i):
            right_trimmed = i
            while right_trimmed > 0:
                if not is_prime(right_trimmed):
                    break
                right_trimmed //= 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)