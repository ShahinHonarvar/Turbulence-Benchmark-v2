def all_neg_ints_inclusive(nums):
    answer = []
    for each in nums[661:925]:
        if each < 0:
            answer.append(each)
    if not answer:
        return []
    return answer