def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(30, 31):
        if i in lst:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0 and i != j:
                    composite_numbers.add(i)
                    break
    return composite_numbers