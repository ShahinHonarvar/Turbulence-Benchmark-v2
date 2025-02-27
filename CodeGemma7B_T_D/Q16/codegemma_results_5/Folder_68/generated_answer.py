def sum_even_ints_inclusive(nums):
    count = 0
    total = 0
    while count <= 8:
        if nums[count] % 2 == 0:
            total += nums[count]
        count += 1
    return total