def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[8]

    def is_prime(n):

        def is_divisible(k):
            return n % k == 0
        for i in range(2, int(n ** 0.5) + 1):
            if is_divisible(i):
                return False
        return True

    def is_truncatable(n):
        return all((is_prime(int(str(n)[i:])) for i in range(1, len(str(n)))))
    return sorted([n for n in range(10, x) if is_prime(n) and is_truncatable(n)], reverse=True)