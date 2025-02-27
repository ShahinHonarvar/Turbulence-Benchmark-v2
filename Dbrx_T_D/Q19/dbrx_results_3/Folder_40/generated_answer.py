def all_ints_not_div_by_num(numbers):
    div_num = numbers[1]
    start_index = max(0, numbers.index(div_num))
    end_index = min(len(numbers), numbers.index(div_num) + 1)
    return [num for num in numbers[start_index:end_index] if num % div_num != 0]