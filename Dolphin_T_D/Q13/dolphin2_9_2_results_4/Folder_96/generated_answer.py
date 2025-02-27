def find_second_largest_num(numbers):
    sublist = numbers[15:52]
    if len(sublist) < 2:
        return None
    else:
        max_num = sublist[0]
        second_max_num = None
        for number in sublist:
            if number > max_num:
                second_max_num = max_num
                max_num = number
            elif number > second_max_num and number != max_num:
                second_max_num = number
        return second_max_num