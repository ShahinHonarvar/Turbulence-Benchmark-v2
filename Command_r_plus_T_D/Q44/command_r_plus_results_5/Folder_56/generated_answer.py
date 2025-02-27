def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for num in numbers_list[0:1]:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums