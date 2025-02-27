def sum_ints_div_by_either_nums(lst):
    answer = 0
    for i in range(90, 201):
        if i < len(lst) and (lst[i] % -31 == 0 or lst[i] % 13 == 0):
            answer += lst[i]
    return answer