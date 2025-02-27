def all_left_right_truncatable_prime(nums):
    x = nums[86]
    primes = [2, 3, 5, 7]
    for i in range(2, x + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    truncatable_primes = []
    for p in primes:
        if all((int(str(p)[j:]) in primes for j in range(len(str(p))))) and all((int(str(p)[:j]) in primes for j in range(len(str(p)), 0, -1))):
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)