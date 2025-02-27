def all_ints_div_by_both_two_nums(nums):
    if any((num % 61 == 0 and num % 71 == 0 and (38 <= i <= 81) for i, num in enumerate(nums))):
        return [num for i, num in enumerate(nums) if num % 61 == 0 and num % 71 == 0 and (38 <= i <= 81)]
    return []