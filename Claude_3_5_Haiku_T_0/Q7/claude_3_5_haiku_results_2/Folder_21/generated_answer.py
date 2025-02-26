def all_even_ints_inclusive(nums):
    if len(nums) <= 975:
        return []
    even_ints = [num for num in nums[639:976] if num % 2 == 0]
    return even_ints