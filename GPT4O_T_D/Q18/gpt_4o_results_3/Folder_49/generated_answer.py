def sum_ints_div_by_either_nums(nums):
    if len(nums) < 81:
        return 0
    total = 0
    for num in nums[80:min(201, len(nums))]:
        if num % 10 == 0 or num % 1000 == 0:
            total += num
    return total