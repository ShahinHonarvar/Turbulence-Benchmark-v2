def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for idx in range(17, 79):
        num = numbers_list[idx]
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums