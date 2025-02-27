def all_left_right_truncatable_prime(nums):

    def is_truncatable(n):
        s = str(n)
        return all((int(s[i:]) in primes and int(s[:-i]) in primes for i in range(1, len(s))))

    def generate_primes(n):
        sieve = [True] * (n + 1)
        for x in range(2, int(n ** 0.5) + 1):
            if sieve[x]:
                for i in range(x * x, n + 1, x):
                    sieve[i] = False
        return [x for x in range(2, n + 1) if sieve[x]]
    x = nums[87]
    primes = set(generate_primes(x))
    return sorted([p for p in primes if is_truncatable(p)])