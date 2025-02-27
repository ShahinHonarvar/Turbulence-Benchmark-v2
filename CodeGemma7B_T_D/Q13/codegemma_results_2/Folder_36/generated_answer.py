def find_second_largest_num(user_list):
    user_list = sorted(user_list)
    if len(user_list) < 246:
        return 'None'
    return user_list[-2]