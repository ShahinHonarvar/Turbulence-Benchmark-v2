def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(281, 695):
        if i < len(numbers):
            if numbers[i] % -722 == 0 or numbers[i] % -731 == 0:
                total += numbers[i]
    return total