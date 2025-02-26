def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    return sum((num for num in nums[:1] if num % 2 == 0))