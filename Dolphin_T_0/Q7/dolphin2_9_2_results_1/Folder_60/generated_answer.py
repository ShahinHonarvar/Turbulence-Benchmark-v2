def all_even_ints_inclusive(nums):
    inclusive_nums = nums[75:86]
    even_nums = [num for num in inclusive_nums if num % 2 == 0]
    return even_nums