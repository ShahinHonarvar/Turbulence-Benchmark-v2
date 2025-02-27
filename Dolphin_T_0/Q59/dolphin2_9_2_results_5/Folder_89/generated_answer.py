def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        for i in range(len(str(n)) - 1, 0, -1):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    prime = [2]
    for n in range(3, t[97]):
        if all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))):
            prime.append(n)
    left_truncatable_prime = [n for n in prime if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_prime, reverse=True)