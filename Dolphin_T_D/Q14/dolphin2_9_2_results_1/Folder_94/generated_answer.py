def find_second_smallest_num(input_list):
    input_list = input_list[52:72]
    if len(input_list) == 0 or len(input_list) == 1:
        return None
    else:
        smallest = min(input_list)
        input_list.remove(smallest)
        second_smallest = min(input_list)
        return second_smallest