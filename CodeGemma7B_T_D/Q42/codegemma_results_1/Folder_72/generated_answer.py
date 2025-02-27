def prime_factors(nums):
    i = 16
    lst = set()
    while nums[i] != 1:
        j = 2
        while nums[i] % j != 0:
            j += 1
        nums[i] //= j
        lst.add(j)
    return lst