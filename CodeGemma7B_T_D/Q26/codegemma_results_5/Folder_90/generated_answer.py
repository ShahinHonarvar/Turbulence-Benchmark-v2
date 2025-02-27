def sum_in_range(nums: list) -> int:
    total = 0
    for num in nums:
        if 273 <= num <= 451:
            total += num
    return total or 0