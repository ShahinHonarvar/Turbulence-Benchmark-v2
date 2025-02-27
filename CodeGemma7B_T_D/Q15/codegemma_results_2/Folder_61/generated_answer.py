def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums[0:8]:
        if num % 2 != 0:
            total += num
    return total if total else 0