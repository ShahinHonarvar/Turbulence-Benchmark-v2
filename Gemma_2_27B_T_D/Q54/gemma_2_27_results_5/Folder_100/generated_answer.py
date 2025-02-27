def all_right_truncatable_prime(nums):
    x = nums[26]
    primes = []
    for i in range(2, x):
        n = i
        is_prime = True
        while n > 0:
            if n < 2 or (n % 2 == 0 and n > 2) or (n % 3 == 0 and n > 3):
                is_prime = False
                break
            n //= 10
        if is_prime:
            primes.append(i)
    return sorted([p for p in primes if all((int(str(p)[:-i]) in primes for i in range(1, len(str(p)))))])