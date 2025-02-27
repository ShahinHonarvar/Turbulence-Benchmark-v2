def gcf_three_nums(nums):
    a = max(nums)
    b = min(nums)
    for n in nums:
        if n > a and n < b:
            a = n
    return a