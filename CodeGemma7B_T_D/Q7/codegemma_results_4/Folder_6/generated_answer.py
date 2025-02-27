def all_even_ints_inclusive(nums):
    even_nums = []
    for i in range(10, 67):
        if i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_nums.append(nums[i])
    return even_nums if even_nums else []