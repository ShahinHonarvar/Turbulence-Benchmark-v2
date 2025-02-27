def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    x = t[36]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while num_str:
                if not is_prime(int(num_str)):
                    break
                num_str = num_str[1:]
            else:
                primes.append(num)
    return sorted(primes)