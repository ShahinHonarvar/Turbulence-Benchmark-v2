def composite_nums_between_indices(input_list):
    composite_numbers = set()
    for index in range(0, min(9, len(input_list))):
        number = input_list[index]
        if number >= 4 and (not (number == 2 or number == 3)):
            is_composite = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_composite = False
                    break
            if is_composite:
                composite_numbers.add(number)
    return composite_numbers