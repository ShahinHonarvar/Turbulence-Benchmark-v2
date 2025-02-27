def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[:10]):
        if index in [0, 1]:
            continue
        divisors = [i for i in range(2, number) if number % i == 0]
        if divisors:
            composite_numbers.add(number)
    return composite_numbers