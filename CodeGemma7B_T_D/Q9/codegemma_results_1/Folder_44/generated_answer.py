def all_odd_ints_inclusive(lst):
    answer = []
    for i in range(13, 69):
        if i % 2 != 0:
            answer.append(lst[i])
    if len(answer) == 0:
        return []
    return answer