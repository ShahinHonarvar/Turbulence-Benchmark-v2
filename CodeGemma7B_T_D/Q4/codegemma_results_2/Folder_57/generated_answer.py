def all_pos_ints_exclusive(nums):
    answer = []
    for n in range(18, 37):
        if n in nums and n > 0:
            answer.append(n)
    return answer