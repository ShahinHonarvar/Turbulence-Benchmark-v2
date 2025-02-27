def sum_ints_div_by_either_nums(nums):
    target_divisors = [55, 10]
    start_index = 58
    end_index = 81
    if len(nums) < end_index + 1:
        return 0
    nums_subset = nums[start_index:end_index + 1]
    sum_divisible = sum((num for num in nums_subset if any((num % divisor == 0 for divisor in target_divisors))))
    return sum_divisible