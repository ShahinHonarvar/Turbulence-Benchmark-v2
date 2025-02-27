def all_even_ints_inclusive(nums):
    even_nums = []
    for num in nums[100:201]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums