def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for index, num in enumerate(numbers_list[37:77], start=37):
        if num > 1 and (not all((num % i for i in range(2, num)))):
            composite_nums.add(num)
    return composite_nums