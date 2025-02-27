def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[39]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            for i in range(len(num_str) - 1, 0, -1):
                if is_prime(int(num_str[:i])):
                    if i == 1:
                        primes.append(num)
            if is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1])):
                primes.append(num)
    return sorted(primes)