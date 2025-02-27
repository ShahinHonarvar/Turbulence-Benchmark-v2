def composite_nums_between_indices(num_list):
    composite_numbers = set()
    for i in range(min(len(num_list), 9)):
        if num_list[i] > 1 and (not num_list[i] & 1) or num_list[i] > 3:
            composite_numbers.add(num_list[i])
    return composite_numbers