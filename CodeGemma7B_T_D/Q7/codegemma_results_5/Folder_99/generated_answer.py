def all_even_ints_inclusive(nums):
    if not nums or len(nums) < 310 or len(nums) < 370:
        return []
    return [num for num in nums if num % 2 == 0 and 310 <= idx(num) <= 370]