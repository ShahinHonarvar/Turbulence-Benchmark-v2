def composite_nums_between_indices(number_list):
    composite_set = set()
    for num in number_list[36:47]:
        if num > 1 and all((num % i != 0 for i in range(2, num))):
            composite_set.add(num)
    return composite_set