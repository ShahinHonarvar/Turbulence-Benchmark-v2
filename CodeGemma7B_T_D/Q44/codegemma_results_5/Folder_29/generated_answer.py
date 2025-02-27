def composite_nums_between_indices(number_list):
    composite_nums = set.intersection((num for num in number_list[52:72] if num % 2), (num for num in number_list[52:72] if num % 3), (num for num in number_list[52:72] if num % 5))
    return composite_nums if composite_nums else set()