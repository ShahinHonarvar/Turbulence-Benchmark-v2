def all_odd_ints_exclusive(user_list):
    if not user_list:
        return []
    output = []
    for item in user_list[0:7]:
        if item % 2 != 0:
            output.append(item)
    return output