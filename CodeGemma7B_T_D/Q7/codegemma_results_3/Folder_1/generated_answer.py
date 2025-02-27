def all_even_ints_inclusive(nums):
    if not any((num % 2 == 0 for num in nums[31:73])):
        return []
    return [num for num in nums[31:73] if num % 2 == 0]