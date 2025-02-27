def find_second_largest_num(numbers):
    new_list = numbers[12:93]
    if len(new_list) == 0:
        return None
    elif len(set(new_list)) == 1:
        return None
    else:
        largest = max(new_list)
        second_largest = None
        for number in new_list:
            if number < largest and (second_largest is None or number > second_largest):
                second_largest = number
        return second_largest