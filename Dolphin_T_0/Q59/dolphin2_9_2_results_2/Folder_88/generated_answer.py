def all_left_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = int_tuple[93]
    left_truncatable_prime = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                left_truncatable_prime.append(i)
    return left_truncatable_prime