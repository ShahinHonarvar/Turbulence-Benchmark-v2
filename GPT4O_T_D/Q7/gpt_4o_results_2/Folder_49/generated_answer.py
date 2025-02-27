def all_even_ints_inclusive(int_list):
    result = []
    if len(int_list) > 200:
        relevant_list = int_list[80:201]
        result = [x for x in relevant_list if x % 2 == 0]
    elif len(int_list) > 80:
        relevant_list = int_list[80:]
        result = [x for x in relevant_list if x % 2 == 0]
    return result