def all_odd_ints_exclusive(nums):
    answer = []
    for i in range(87, 100):
        if nums[i] % 2 != 0:
            answer.append(nums[i])
    return answer