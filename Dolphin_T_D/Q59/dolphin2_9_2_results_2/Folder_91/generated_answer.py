def all_left_truncatable_prime(linear_sequence):
    x = linear_sequence[0]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i, w = (5, 2)
        while i * i <= n:
            if n % i == 0:
                return False
            if w == 2:
                w = 4
                i += 2
            else:
                w = 2
                i += 4
        return True

    def is_left_truncatable_prime(n):
        return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))
    prime_numbers = []
    for n in reversed(range(2, x)):
        if is_left_truncatable_prime(n):
            prime_numbers.append(n)
    return prime_numbers