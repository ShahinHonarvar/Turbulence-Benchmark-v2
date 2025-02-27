def find_second_largest_num(num_list):
    try:
        num_list = [int(x) for x in num_list]
    except ValueError:
        return 'None'
    filtered_list = [x for x in num_list if 40 <= x <= 200]
    filtered_list.sort(reverse=True)
    return filtered_list[1] if len(filtered_list) > 1 else 'None'