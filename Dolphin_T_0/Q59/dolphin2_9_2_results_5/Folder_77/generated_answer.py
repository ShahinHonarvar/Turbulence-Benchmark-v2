def all_left_truncatable_prime(nums):
    x = nums[767]
    primes = [n for n in range(2, x) if all((n % i != 0 for i in range(2, n)))]
    left_trunc_primes = [n for n in primes if all((int(str(n)[i:]) in primes for i in range(1, len(str(n)))))]
    return sorted(left_trunc_primes, reverse=True)