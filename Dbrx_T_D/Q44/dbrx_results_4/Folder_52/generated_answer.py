def composite_nums_between_indices(numbers_list):
    composite_numbers = set()
    for i in range(62, 100):
        if i < len(numbers_list) and numbers_list[i] > 1:
            if not numbers_list[i] % 2 == 0 or numbers_list[i] == 2:
                for j in range(3, int(numbers_list[i] ** 0.5) + 1, 2):
                    if numbers_list[i] % j == 0:
                        break
                else:
                    composite_numbers.add(numbers_list[i])
    return composite_numbers