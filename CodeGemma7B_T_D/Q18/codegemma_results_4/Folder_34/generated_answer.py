def sum_ints_div_by_either_nums(num_list):
    answer = 0
    for num in num_list[60:201]:
        if num % 9 == 0 or num % 11 == 0:
            answer += num
    return answer