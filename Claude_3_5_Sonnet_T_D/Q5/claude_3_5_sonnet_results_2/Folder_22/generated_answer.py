def all_neg_ints_inclusive(integer_list):
    start_index = 40
    end_index = 201
    result = []
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] < 0:
            result.append(integer_list[i])
    return result