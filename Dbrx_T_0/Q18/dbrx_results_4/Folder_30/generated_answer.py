def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 11 or i > 76:
            continue
        if numbers[i] % -81 == 0 or numbers[i] % -94 == 0:
            return sum((x for x in numbers[11:77] if x % -81 == 0 or x % -94 == 0))
    return 0