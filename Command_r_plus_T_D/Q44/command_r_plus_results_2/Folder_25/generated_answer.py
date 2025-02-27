def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for idx in range(75, 95):
        num = numbers_list[idx]
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            continue
        composite_nums.add(num)
    return composite_nums