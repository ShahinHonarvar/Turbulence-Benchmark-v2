def sum_in_range(nums):
    total = 0
    for num in nums:
        if 86 <= num <= 90:
            total += num
    return total if total != 0 else 0