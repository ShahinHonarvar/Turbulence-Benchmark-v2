def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for num in numbers_list[50:55]:
        if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
            composite_numbers.add(num)
    return composite_numbers