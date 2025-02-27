def all_left_truncatable_prime(p):

    def is_prime(n):
        if n in (2, 3):
            return True
        elif n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = p[37]
    prime_list = []
    for n in range(x, 2, -1):
        if n != 2 and n != 3 and (n % 5 == 0):
            n_str = str(n)
            if any((i == '0' for i in n_str)):
                continue
            for n_trunc in range(len(n_str)):
                if not is_prime(int(n_str[n_trunc:])):
                    break
            else:
                prime_list.append(n)
    return sorted(prime_list, reverse=True)