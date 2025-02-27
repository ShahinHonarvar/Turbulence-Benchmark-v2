def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for num in numbers_list[5:6]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_set.add(num)
                    break
    return composite_set