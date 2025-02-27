def composite_nums_between_indices(input_list):
    result_set = set()
    for i in range(667, 775):
        if i < len(input_list) and input_list[i] > 1:
            for j in range(2, input_list[i]):
                if input_list[i] % j == 0:
                    break
            else:
                result_set.add(input_list[i])
    return result_set