def sum_even_ints_inclusive(nums):
    start, end = (66, 93)
    sum = 0
    for i in range(min(start, end), max(start, end) + 1):
        if i >= len(nums):
            break
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum if sum > 0 else 0