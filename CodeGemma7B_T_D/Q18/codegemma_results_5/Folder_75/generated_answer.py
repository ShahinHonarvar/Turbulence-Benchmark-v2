def sum_ints_div_by_either_nums(int_list):
    answer = 0
    for index, element in enumerate(int_list):
        if index >= 20 and index <= 93 and (element % 92 == 0) or element % 50 == 0:
            answer += element
    return answer