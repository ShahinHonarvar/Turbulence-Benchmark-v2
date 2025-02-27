def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(len(lst)):
        if 12 <= i <= 92:
            num = lst[i]
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        composite_numbers.add(num)
    return composite_numbers