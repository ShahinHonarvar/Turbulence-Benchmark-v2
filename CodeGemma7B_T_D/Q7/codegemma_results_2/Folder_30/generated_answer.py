def all_even_ints_inclusive(user_list):
    result = []
    for i in user_list[55:99]:
        if i % 2 == 0:
            result.append(i)
    return result