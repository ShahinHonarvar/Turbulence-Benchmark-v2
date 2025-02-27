def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[81]
    prime_list = []
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
                if trunc == 1:
                    prime_list.append(i)
    return sorted(prime_list, reverse=True)