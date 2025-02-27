def sum_even_ints_inclusive(nums):
    total = sum((num for num in nums[74:96] if num % 2 == 0))
    return total if total else 0