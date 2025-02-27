def all_even_ints_inclusive(nums):
    start, end = (34, 55)
    evens = [num for num in nums[start:end + 1] if num % 2 == 0]
    return evens