def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[87]
    left_right_truncatable_primes = []
    for i in range(x, 1, -1):
        if '0' not in str(i) and is_prime(i):
            test = i
            while len(str(test)) > 1:
                if not is_prime(test):
                    break
                test = int(str(test)[1:-1])
            else:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)