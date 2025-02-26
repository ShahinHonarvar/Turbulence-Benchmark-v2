def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[543:585] if num % -553 == 0 and num % -737 == 0]
    return result