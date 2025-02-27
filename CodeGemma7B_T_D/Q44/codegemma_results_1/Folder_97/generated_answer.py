def composite_nums_between_indices(lst):
    composite = set()
    for number in lst:
        if 15 <= lst.index(number) <= 39:
            for divisor in range(2, number):
                if number % divisor == 0:
                    composite.add(number)
                    break
    return composite