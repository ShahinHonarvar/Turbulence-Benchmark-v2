def composite_nums_between_indices(num_list):
    result = set()
    for i in range(len(num_list)):
        if i >= 60 and i <= 200:
            if num_list[i] > 1 and (not num_list[i] & 1) and (num_list[i] % 3 != 0) or (num_list[i] % 5 == 0 and num_list[i] != 5) or (num_list[i] % 7 == 0 and num_list[i] != 7):
                result.add(num_list[i])
    return result