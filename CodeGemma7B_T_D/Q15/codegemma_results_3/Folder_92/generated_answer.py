def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums:
        if num % 2 != 0 and 1 <= nums.index(num) <= len(nums):
            total += num
    return total if total != 0 else 0