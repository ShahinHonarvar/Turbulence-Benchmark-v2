def find_second_smallest_num(input_list):
    if not input_list:
        return None
    elif len(input_list) < 2:
        return None
    input_list = input_list[62:93]
    input_list.sort()
    distinct_numbers = list(set(input_list))
    distinct_numbers.sort()
    if len(distinct_numbers) < 2:
        return None
    else:
        return distinct_numbers[1]