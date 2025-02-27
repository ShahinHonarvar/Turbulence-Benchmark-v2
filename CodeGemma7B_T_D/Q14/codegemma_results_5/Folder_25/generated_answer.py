def find_second_smallest_num(user_list):
    if len(user_list) > 36 and len(user_list) < 77:
        user_list.sort()
        return user_list[36]
    else:
        return 'None'