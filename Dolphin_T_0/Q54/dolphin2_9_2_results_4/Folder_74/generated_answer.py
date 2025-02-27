def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[36]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            string_num = str(i)
            for j in range(len(string_num) - 1, 0, -1):
                if is_prime(int(string_num[0:j])):
                    primes.append(i)
    return sorted(primes)