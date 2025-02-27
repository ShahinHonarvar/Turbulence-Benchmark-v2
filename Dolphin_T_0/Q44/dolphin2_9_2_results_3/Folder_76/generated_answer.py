def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(639, 976):
        num = lst[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_numbers.add(num)
                    break
    return composite_numbers