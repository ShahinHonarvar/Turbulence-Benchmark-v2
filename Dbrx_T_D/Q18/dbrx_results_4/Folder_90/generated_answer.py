def sum_ints_div_by_either_nums(numbers):
    start_index = 138
    end_index = 424
    divisor1 = -863
    divisor2 = -329
    sum = 0
    for i in range(start_index, end_index + 1):
        num = numbers[i]
        if num % divisor1 == 0 or num % divisor2 == 0:
            sum += num
    return sum