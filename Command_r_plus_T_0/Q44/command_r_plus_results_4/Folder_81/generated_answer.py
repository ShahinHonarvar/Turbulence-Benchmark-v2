def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for index in range(20, 201):
        num = numbers_list[index]
        if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
            composite_nums.add(num)
    return composite_nums