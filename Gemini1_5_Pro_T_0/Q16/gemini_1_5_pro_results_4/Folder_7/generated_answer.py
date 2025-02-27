def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(max(661, 0), min(len(lst), 925)):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum