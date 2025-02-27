def all_neg_ints_inclusive(int_list):
    start = 527
    end = 538
    result = []
    for i in range(start, end + 1):
        if i < len(int_list) and int_list[i] < 0:
            result.append(int_list[i])
    return result