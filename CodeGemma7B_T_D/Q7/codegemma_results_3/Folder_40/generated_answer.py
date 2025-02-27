def all_even_ints_inclusive(nums):
    answer = []
    for i in range(0, 3):
        if nums[i] % 2 == 0:
            answer.append(nums[i])
    return answer