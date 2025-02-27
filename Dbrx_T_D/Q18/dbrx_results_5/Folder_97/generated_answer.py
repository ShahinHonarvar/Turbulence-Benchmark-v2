def sum_ints_div_by_either_nums(numbers):
    for i in range(len(numbers)):
        if i < 58 or i > 75:
            continue
        num = numbers[i]
        if num % 72 == 0 or num % 62 == 0:
            if 'total' not in locals():
                total = num
            else:
                total += num
    if 'total' not in locals():
        return 0
    return total