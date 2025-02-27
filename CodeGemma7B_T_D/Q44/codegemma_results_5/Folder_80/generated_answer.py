def composite_nums_between_indices(int_list):
    composites = set()
    for num in int_list[62:79]:
        if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composites.add(num)
    return composites