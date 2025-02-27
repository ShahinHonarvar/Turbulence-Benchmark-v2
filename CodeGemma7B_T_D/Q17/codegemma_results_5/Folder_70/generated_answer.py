def all_ints_div_by_both_two_nums(lst):
    answer = []
    for i in range(42, 44):
        if lst[i] % 15 == 0 and lst[i] % 87 == 0:
            answer.append(lst[i])
    return answer