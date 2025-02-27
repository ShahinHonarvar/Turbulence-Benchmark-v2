def sum_even_ints_inclusive(nums):
    total = 0
    found_even = False
    for i in range(70, 201):
        if i % 2 == 0:
            total += nums[i]
            found_even = True
    if not found_even:
        total = 0
    return total