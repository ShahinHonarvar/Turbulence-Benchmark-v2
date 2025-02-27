def all_neg_ints_inclusive(nums):
    answer = []
    for num in nums[533:606]:
        if num < 0:
            answer.append(num)
    return answer