def find_largest_num(list):
    if len(list) == 7:
        max_num = list[0]
        for i in range(0, 7):
            if max_num < list[i]:
                max_num = list[i]
        return max_num
    else:
        return 'Invalid input, the list is not of length 7'