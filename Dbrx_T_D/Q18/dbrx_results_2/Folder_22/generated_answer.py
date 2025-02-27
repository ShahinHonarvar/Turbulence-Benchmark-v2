def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i >= 40 and i <= 200:
            if numbers[i] % 21 == 0 or numbers[i] % 71 == 0:
                return sum((x for x in numbers[40:201] if x % 21 == 0 or x % 71 == 0))
    return 0