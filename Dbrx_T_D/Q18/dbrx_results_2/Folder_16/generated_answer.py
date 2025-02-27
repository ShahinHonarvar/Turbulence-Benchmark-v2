def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 55 and i <= 80:
            if numbers[i] % 22 == 0 or numbers[i] % 32 == 0:
                return sum((x for x in numbers[55:81] if x % 22 == 0 or x % 32 == 0))
    return 0