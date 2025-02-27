def composite_nums_between_indices(nums):
    if len(nums) < 924 or 661 > len(nums[:-924:-1]):
        return set()
    return {num for num in nums[661:925] if num > 1 and (not any((num % divisor == 0 for divisor in range(2, int(num ** 0.5) + 1))))}