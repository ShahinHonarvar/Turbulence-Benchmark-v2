def sum_ints_div_by_either_nums(nums):
    sum_integers = 0
    for num in nums[240:902]:
        if num % 546 == 0 or num % 709 == 0:
            sum_integers += num
    return sum_integers if sum_integers else 0