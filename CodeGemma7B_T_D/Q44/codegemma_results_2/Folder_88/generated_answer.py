def composite_nums_between_indices(int_list):
    composite_set = set()
    for index in range(8, 10):
        if index >= len(int_list):
            continue
        number = int_list[index]
        if number > 1:
            for divisor in range(2, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    composite_set.add(number)
                    break
    return composite_set