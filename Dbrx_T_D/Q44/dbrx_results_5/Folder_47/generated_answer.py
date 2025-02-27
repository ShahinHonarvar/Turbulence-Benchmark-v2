def composite_nums_between_indices(num_list):
    composite_numbers = set()
    for i in range(len(num_list)):
        if i >= 75 and i <= 88:
            num = num_list[i]
            if num > 1 and (not num % 2 == 0) or not num % 3 == 0:
                if num > 2:
                    composite_numbers.add(num)
    return composite_numbers