def sum_even_ints_inclusive(nums):
    evens = [num for num in nums[10:101] if num % 2 == 0]
    if not evens:
        return 0
    return sum(evens)