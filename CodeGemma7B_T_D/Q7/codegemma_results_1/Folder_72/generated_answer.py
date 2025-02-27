def all_even_ints_inclusive(nums):
    i = 29
    j = 51
    even_nums = []
    while i <= j:
        if nums[i] % 2 == 0:
            even_nums.append(nums[i])
        i += 1
    return even_nums