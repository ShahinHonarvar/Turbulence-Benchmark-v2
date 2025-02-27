def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_nums = set()
    for index in range(69, 84):
        num = numbers_list[index]
        if num > 1 and (not all((num % i for i in range(2, num)))):
            composite_nums.add(num)
    return composite_nums