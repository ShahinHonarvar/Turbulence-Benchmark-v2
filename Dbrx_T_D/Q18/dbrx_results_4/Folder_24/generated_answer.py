def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 29 or i > 53:
            continue
        if numbers[i] % -68 == 0 or numbers[i] % -85 == 0:
            return sum((x for x in numbers[29:54] if x % -68 == 0 or x % -85 == 0))
    return 0