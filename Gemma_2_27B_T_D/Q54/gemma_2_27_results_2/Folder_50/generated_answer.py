def all_right_truncatable_prime(t):
    x = t[57]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(x - 1, 1, -1):
        if str(i).isdigit() and is_prime(i):
            is_truncatable = True
            for j in range(len(str(i)) - 1, 0, -1):
                if not is_prime(int(str(i)[:j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes