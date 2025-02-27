def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index in range(27, 56):
        num = numbers_list[index]
        if num > 1 and (not all((num % i for i in range(2, num)))):
            composite_numbers.add(num)
    return composite_numbers