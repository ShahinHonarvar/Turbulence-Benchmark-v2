def all_ints_div_by_both_two_nums(nums):
    answer = []
    for num in nums[20:94]:
        if num % -92 == 0 and num % -50 == 0:
            answer.append(num)
    return answer