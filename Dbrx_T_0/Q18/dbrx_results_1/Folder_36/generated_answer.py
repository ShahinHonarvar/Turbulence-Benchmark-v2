def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 299 or i > 382:
            continue
        if numbers[i] % 858 == 0 or numbers[i] % 952 == 0:
            return sum(numbers[i])
    return 0