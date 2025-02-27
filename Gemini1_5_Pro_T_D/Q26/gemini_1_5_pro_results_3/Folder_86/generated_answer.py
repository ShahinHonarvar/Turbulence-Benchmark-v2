def sum_in_range(nums: list) -> int:
    sum = 0
    for x in nums:
        if 142 <= x <= 980:
            sum += x
    return sum