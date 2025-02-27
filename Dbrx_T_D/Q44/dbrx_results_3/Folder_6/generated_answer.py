def composite_nums_between_indices(num_list):
    composite_numbers = set()
    for i in range(13, 69):
        if i < len(num_list) and num_list[i] > 1:
            for j in range(2, num_list[i]):
                if num_list[i] % j == 0:
                    composite_numbers.add(num_list[i])
                    break
    return composite_numbers