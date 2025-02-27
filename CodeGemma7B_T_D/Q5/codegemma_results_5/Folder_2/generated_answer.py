def all_neg_ints_inclusive(l):
    answer = []
    for i in range(15, 40):
        if l[i] < 0:
            answer.append(l[i])
    return answer