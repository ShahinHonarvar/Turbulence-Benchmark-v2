def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 18 and i <= 52:
            num = numbers[i]
            if num % 15 == 0 or num % 57 == 0:
                total += num
    return total