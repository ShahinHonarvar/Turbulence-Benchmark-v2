def sum_even_ints_inclusive(nums):
    even_ints = [num for num in nums[1:6] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0