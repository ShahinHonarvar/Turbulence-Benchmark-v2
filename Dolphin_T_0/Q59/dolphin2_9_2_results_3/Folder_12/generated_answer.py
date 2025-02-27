def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[70]
    left_truncatable_prime = [i for i in range(x, 0, -1) if is_prime(i) and (not '0' in str(i))]
    for prime in left_truncatable_prime:
        i = 1
        while True:
            if not is_prime(int(str(prime)[i:])):
                left_truncatable_prime.remove(prime)
                break
            i += 1
    return sorted(left_truncatable_prime, reverse=True)