def gcf_three_nums(nums):
    a = nums[64]
    b = nums[80]
    c = nums[15]
    factors = list(set(factorize(a)).intersection(set(factorize(b)).intersection(set(factorize(c)))))
    return max(factors)