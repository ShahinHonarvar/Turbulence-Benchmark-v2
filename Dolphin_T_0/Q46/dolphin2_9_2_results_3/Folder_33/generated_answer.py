def gcf_three_nums(nums):
    a = nums[252]
    b = nums[149]
    c = nums[564]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    if a == 1:
        return 1
    else:
        c_factors = []
        i = 2
        while i <= c:
            if c % i == 0:
                c_factors.append(i)
                c //= i
            i += 1
        common_factors = set(c_factors) & set([a] + c_factors)
        return max(common_factors)