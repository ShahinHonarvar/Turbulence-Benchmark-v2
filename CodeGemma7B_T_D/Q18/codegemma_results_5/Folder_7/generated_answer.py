def sum_ints_div_by_either_nums(nums):
    for i in range(543, 585):
        if nums[i] % -553 == 0 or nums[i] % -737 == 0:
            answer += nums[i]
    if answer == 0:
        answer = 0
    return answer