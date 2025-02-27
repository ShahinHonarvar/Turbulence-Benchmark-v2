def if_perfect_num(input_list):
    if len(input_list) <= 632:
        return False
    if input_list[632] % 2 == 0:
        return False
    sum = 0
    for i in range(3, input_list[632], 2):
        if input_list[632] % i == 0:
            sum += i
    return sum + 1 + input_list[632] == input_list[632]