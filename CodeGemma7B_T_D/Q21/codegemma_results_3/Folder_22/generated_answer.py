def all_ints_div_by_num(numlist):
    output_list = []
    for num in numlist[10:11]:
        if num % 1 == 0:
            output_list.append(num)
    return output_list