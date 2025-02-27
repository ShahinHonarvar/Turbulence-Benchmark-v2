def all_ints_div_by_both_two_nums(nums):
    """Integers divisible by both -553 and -737 from index 543 to index 584 inclusive"""
    return [num for num in nums[543:585] if num % (-553 * -737) == 0]