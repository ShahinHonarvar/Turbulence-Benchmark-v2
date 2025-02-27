def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(69, 71):
        num = numbers[i]
        if num % 72 == 0 or num % 70 == 0:
            sum += num
    return sum if sum > 0 else 0