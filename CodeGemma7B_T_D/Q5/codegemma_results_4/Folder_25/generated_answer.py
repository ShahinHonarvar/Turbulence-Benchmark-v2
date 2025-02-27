def all_neg_ints_inclusive(lst):
    answer = []
    for i in range(29, 94):
        if lst[i] < 0:
            answer.append(lst[i])
    return answer