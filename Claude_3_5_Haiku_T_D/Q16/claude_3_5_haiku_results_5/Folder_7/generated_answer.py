def sum_even_ints_inclusive(nums):
    if len(nums) <= 924:
        return 0
    even_sum = sum((num for num in nums[661:925] if num % 2 == 0))
    return even_sum