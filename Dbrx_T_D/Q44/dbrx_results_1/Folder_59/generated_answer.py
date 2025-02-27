def composite_nums_between_indices(n_list):
    composite_numbers = {num for num in n_list if num >= 0 and num <= 9 and (num > 1 and (not num & 1) and all((num % i for i in range(3, int(num ** 0.5) + 1, 2)))) or (num > 3 and num % 2 == 0)}
    return set(composite_numbers)