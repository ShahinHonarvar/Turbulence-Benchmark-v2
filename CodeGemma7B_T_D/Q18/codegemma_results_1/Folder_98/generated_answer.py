def sum_ints_div_by_either_nums(nums):
    answer = 0
    for i in range(0, 6):
        if nums[i] % -1 == 0 or nums[i] % 13 == 0:
            answer += nums[i]
    return answer