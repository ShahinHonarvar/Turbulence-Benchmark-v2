def composite_nums_between_indices(my_list):
    composite_numbers = set()
    for i in range(29, 94):
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    composite_numbers.add(my_list[i])
                    break
    return composite_numbers