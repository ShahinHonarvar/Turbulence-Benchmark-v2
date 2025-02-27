def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for idx in range(15, 40):
        num = numbers_list[idx]
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums