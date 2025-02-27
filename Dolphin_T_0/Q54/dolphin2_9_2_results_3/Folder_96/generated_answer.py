def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[29]
    right_truncatable_primes = [str(i) for i in range(2, x) if is_prime(i)]
    for i in range(len(right_truncatable_primes)):
        for j in range(len(right_truncatable_primes[i]) - 1, 0, -1):
            if not is_prime(int(right_truncatable_primes[i][:j])):
                right_truncatable_primes.remove(right_truncatable_primes[i])
                break
    return sorted(list(map(int, right_truncatable_primes)), default=None)