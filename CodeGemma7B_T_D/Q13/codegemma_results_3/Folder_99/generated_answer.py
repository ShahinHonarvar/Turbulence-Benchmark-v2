def find_second_largest_num(user_list):
    user_list.sort(reverse=True)
    try:
        return user_list[310:371][1]
    except IndexError:
        return None