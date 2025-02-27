def composite_nums_between_indices(input_list):
    composite_numbers = set()
    for i in range(min(5, len(input_list))):
        if input_list[i] > 1 and all((input_list[i] % j != 0 for j in range(2, input_list[i]))):
            for j in range(i, min(i + 7, len(input_list))):
                if input_list[j] > 1 and all((input_list[j] % k != 0 for k in range(2, input_list[j]))):
                    composite_numbers.add(input_list[j])
    return composite_numbers