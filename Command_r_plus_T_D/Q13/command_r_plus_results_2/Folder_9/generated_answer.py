def find_second_largest_num(num_list: list[int]) -> int:
    if len(num_list) < 201:
        return None
    else:
        sub_list = num_list[200:202]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None