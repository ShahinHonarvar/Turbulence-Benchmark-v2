def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, round(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[19]
    primes = []
    for i in range(1, x):
        i_str = str(i)
        if '0' in i_str:
            continue
        for j in range(len(i_str)):
            if not is_prime(int(i_str[j:])):
                break
            if j == len(i_str) - 1:
                primes.append(i)
    return sorted(primes)