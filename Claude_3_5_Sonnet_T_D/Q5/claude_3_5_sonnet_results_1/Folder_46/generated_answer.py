def all_neg_ints_inclusive(integer_list):
    start_index = 30
    end_index = 88
    result = []
    if len(integer_list) > start_index:
        for num in integer_list[start_index:end_index]:
            if num < 0:
                result.append(num)
    return result