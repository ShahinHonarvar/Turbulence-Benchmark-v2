def all_even_ints_exclusive(nums):
    evens = [num for num in nums[90:200] if num % 2 == 0]
    return evens if len(evens) > 0 else []