def composite_nums_between_indices(int_list):
    composite_nums = set()
    for num in int_list[56:67]:
        if num != 1 and num % 2 != 0 and all((num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2))):
            composite_nums.add(num)
    return composite_nums