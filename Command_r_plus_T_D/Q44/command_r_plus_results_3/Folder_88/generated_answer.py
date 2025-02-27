def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_nums_in_range = set()
    for num in numbers_list[8:10]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    composite_nums_in_range.add(num)
                    break
    return composite_nums_in_range