def composite_nums_between_indices(input_list):
    return set((num for num, idx in enumerate(input_list[30:88], 30) if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))))