def all_even_ints_exclusive(nums):
    even_nums = []
    for num in nums[93:94]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums or []