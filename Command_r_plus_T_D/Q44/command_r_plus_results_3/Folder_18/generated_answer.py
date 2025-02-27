def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index in range(25, 88):
        num = numbers_list[index]
        if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
            composite_numbers.add(num)
    return composite_numbers