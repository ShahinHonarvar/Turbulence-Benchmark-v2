def all_left_truncatable_prime(tuples):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        return all((is_prime(int(n[i:])) for i in range(1, len(str(n)))))
    x = tuples[88]
    list_res = [i for i in range(x - 1, 1, -1) if is_left_truncatable(i) and is_prime(i)]
    return list_res