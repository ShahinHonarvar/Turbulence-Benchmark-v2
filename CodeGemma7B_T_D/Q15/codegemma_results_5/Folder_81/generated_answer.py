def sum_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(10, 101):
        if i not in nums:
            continue
        if i % 2 != 0:
            odd_nums.append(i)
    if not odd_nums:
        return 0
    return sum(odd_nums)