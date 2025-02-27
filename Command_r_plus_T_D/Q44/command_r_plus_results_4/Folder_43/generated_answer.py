def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_nums = set()
    for index, num in enumerate(numbers_list[31:73], start=31):
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums