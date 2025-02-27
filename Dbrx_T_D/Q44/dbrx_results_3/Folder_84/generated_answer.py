def composite_nums_between_indices(num_list):
    composite_numbers = set()
    for i in range(len(num_list)):
        if i >= 30 and i <= 48:
            if num_list[i] > 1 and (not num_list[i] == 2) and (not num_list[i] == 3):
                for j in range(2, int(num_list[i] ** 0.5) + 1):
                    if num_list[i] % j == 0:
                        composite_numbers.add(num_list[i])
                        break
    return composite_numbers