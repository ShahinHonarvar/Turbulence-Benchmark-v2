def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index in range(10, 67):
        num = numbers_list[index]
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_numbers.add(num)
                break
    return composite_numbers