def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums[82:87]:
        if num % 2 == 0:
            even_nums.append(num)
    if len(even_nums) == 0:
        return []
    return even_nums