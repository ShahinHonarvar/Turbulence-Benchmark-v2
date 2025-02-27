def all_odd_ints_inclusive(lst):
    answer = []
    for i in range(37, 77):
        if lst[i] % 2 != 0:
            answer.append(lst[i])
    return answer