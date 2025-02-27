def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[96]
    left_truncatables = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                left_truncatables.append(i)
    return sorted(left_truncatables, reverse=True)