def composite_nums_between_indices(lst):
    composite_numbers = set()
    for num, i in enumerate(lst):
        if num >= 25 and num <= 59:
            for j in range(2, i):
                if i % j == 0:
                    composite_numbers.add(i)
                    break
    return composite_numbers