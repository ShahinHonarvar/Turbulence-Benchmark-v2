def all_ints_not_div_by_num(list1):
    answer = []
    for num in list1[24:25]:
        if num % 30 != 0:
            answer.append(num)
    return answer