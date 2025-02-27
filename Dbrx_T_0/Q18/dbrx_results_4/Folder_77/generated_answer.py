def sum_ints_div_by_either_nums(numbers):
    start_index = 828
    end_index = 932
    divisor1 = -649
    divisor2 = -461
    sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(numbers) and (numbers[i] % divisor1 == 0 or numbers[i] % divisor2 == 0):
            sum += numbers[i]
    return sum