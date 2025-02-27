def sum_even_ints_inclusive(nums):
    start = 59
    end = 97
    total = 0
    for i in range(min(start, end), max(start, end) + 1):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            total += nums[i]
    return total