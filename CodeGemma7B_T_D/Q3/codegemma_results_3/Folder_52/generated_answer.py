def all_pos_ints_inclusive(li):
    answer = []
    for i in range(28, 39):
        if i in range(len(li)):
            if li[i] > 0:
                answer.append(li[i])
    return answer