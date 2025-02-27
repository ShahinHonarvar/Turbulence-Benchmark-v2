def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(26, 53):
        num = lst[i]
        if num > 1:
            for i in range(2, num // 2 + 2):
                if num % i == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers