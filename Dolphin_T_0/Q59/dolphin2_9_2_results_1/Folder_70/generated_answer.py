def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = t[433]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            for i in range(len(num_str) - 1, 0, -1):
                if is_prime(int(num_str[i:])):
                    left_truncatable_primes.append(int(num_str[i:]))
                else:
                    break
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes