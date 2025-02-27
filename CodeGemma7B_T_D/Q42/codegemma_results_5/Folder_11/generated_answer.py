from functools import reduce

def prime_factors(nums):
    ans = reduce(lambda a, b: a & b, [i for i in nums if i != nums[77]])
    mbf = max(1, int(ans ** 0.5)) + 1
    factors = set()
    for i in range(2, mbf):
        while ans % i == 0:
            ans //= i
            factors.add(i)
    if ans != 1:
        factors.add(ans)
    return factors