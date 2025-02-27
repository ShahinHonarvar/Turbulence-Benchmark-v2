def all_even_ints_exclusive(nums):
    output = []
    for i in range(15, 100):
        if nums[i] % 2 == 0:
            output.append(nums[i])
    return output