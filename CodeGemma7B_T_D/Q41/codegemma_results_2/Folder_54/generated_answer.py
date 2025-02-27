def identical_elements(first_list, second_list):
    result_set = set()
    for i in range(34, 56):
        if first_list[i] in second_list[i]:
            result_set.add(first_list[i])
    return result_set