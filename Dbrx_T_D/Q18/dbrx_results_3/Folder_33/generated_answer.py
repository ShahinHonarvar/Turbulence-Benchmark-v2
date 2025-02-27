def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(len(numbers)):
        if i >= 281 and i <= 694:
            num = numbers[i]
            if num % -722 == 0 or num % -731 == 0:
                total += num
    return total