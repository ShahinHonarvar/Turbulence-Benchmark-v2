def sum_even_ints_inclusive(lst):
    lst = lst[56:58]
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum if sum != 0 else 0