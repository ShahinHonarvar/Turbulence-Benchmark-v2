def all_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = int_tuple[433]
    prime_list = []
    for n in range(2, x):
        if is_prime(n):
            n_list = list(str(n))
            for i in range(len(n_list)):
                if int(''.join(n_list[i:])) != n:
                    break
                else:
                    continue
            else:
                prime_list.append(n)
    return sorted(prime_list, reverse=True)