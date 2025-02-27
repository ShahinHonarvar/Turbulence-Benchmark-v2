def all_odd_ints_inclusive(num_list):
    official_list = num_list[19:93]
    filtered_list = []
    if official_list:
        for value in official_list:
            if value % 2 != 0:
                filtered_list.append(value)
        return filtered_list
    return []