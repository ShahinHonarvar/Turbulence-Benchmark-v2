def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[543:585]:
        if num % -553 == 0 or num % -737 == 0:
            sum += num
    return sum or 0