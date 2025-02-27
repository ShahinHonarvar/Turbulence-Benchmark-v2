def all_left_truncatable_prime(tp):
    x = tp[88]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i] == '0' or not is_prime(int(str_n[:i])):
                return False
        return True
    filtered_primes = [p for p in range(2, x) if is_prime(p) and is_left_truncatable_prime(p)]
    filtered_primes.sort()
    return filtered_primes