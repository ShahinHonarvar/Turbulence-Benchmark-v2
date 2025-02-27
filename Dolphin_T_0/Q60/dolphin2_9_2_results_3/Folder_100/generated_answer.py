def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_lr_truncatable(n):
        if n <= 11:
            return False
        n_str = str(n)
        for i in range(len(n_str)):
            for j in range(i + 2, len(n_str) + 1):
                substr = n_str[i:j]
                if is_prime(int(substr)):
                    if i != 0 or j != len(n_str):
                        continue
                else:
                    return False
            if i != 0 or j != len(n_str):
                continue
            if is_prime(int(n_str[i:])) and is_prime(int(n_str[:j])):
                return True
        return False
    x = t[26]
    lr_truncatable_primes = []
    for i in range(2, x + 1):
        if is_lr_truncatable(i):
            lr_truncatable_primes.append(i)
    return sorted(lr_truncatable_primes)