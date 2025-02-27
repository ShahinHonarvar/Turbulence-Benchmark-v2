def find_second_smallest_num(num_list):
    if 527 <= len(num_list) <= 538:
        num_list = num_list[527:539]
        num_list = list(set(num_list))
        num_list.sort()
        if len(num_list) < 2:
            return None
        else:
            return num_list[1]
    else:
        return None