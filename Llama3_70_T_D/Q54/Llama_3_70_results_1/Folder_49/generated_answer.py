def all_right_truncatable_prime(nums):
    primes = set()
    for i in range(2, nums[14]):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)

    def is_right_truncatable(p):
        p = str(p)
        for i in range(len(p)):
            if int(p[:len(p) - i]) not in primes:
                return False
        return True
    return sorted([p for p in primes if is_right_truncatable(p)])