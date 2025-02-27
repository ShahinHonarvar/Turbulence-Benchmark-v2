def sum_ints_div_by_either_nums(numbers):
    start_index = 315
    end_index = 934
    target_divisors = (-897, -556)
    sum_result = 0
    for i in range(start_index, end_index + 1):
        num = numbers[i]
        if num % target_divisors[0] == 0 or num % target_divisors[1] == 0:
            sum_result += num
    return sum_result