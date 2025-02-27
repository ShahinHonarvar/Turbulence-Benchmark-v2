def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[32]
    primes_less_than_x = []
    for n in range(2, x):
        if is_prime(n):
            s = str(n)
            if '0' in s:
                continue
            for i in range(len(s) - 1):
                if not is_prime(int(s[i:])):
                    break
            else:
                primes_less_than_x.append(n)
    return primes_less_than_x