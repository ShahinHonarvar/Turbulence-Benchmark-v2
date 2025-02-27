def composite_nums_between_indices(l):
    return set([num for num in l[28:33] if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))])