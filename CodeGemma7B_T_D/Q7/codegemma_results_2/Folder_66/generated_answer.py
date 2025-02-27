def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums[50:55]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums or []