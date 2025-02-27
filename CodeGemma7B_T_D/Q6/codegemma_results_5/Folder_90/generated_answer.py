def all_neg_ints_exclusive(nums):
    answer = []
    for i in range(389, 748):
        if nums[i] < 0:
            answer.append(nums[i])
    if not answer:
        answer = []
    return answer