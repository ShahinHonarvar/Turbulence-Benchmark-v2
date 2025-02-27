def all_left_truncatable_prime(nums):
    x = nums[645]
    primes = set(range2(2, x))
    lst = []
    for p in primes:
        if p in (0, 2, 5):
            continue
        if int(str(p)[::-1]) not in primes:
            continue
        n = p
        while n > 0:
            if n not in primes or '0' in str(n):
                break
            n //= 10
        if n > 0:
            lst.append(p)
    lst.sort()
    return lst