def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, num in enumerate(numbers_list):
        if index >= 64 and index <= 66:
            if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
                composite_numbers.add(num)
    return composite_numbers