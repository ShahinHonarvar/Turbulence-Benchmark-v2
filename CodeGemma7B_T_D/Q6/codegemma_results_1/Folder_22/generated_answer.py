def all_neg_ints_exclusive(num_list):
    answer = []
    for i in range(40, 200):
        if num_list[i] < 0:
            answer.append(num_list[i])
    return answer