def all_pos_ints_exclusive(nums):
    answer = []
    for num in nums:
        if 49 < num < 74 and num > 0:
            answer.append(num)
    return answer