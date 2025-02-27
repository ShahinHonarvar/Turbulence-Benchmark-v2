def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums[22:51]:
        if num % 2 == 0:
            even_nums.append(num)
    if not even_nums:
        return []
    return even_nums