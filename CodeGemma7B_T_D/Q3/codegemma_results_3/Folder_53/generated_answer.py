def all_pos_ints_inclusive(nums):
    answer = []
    for num in nums:
        if 100 <= num <= 200:
            answer.append(num)
    return answer if answer else []