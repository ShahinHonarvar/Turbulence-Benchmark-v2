def find_second_smallest_num(numbers):
    if len(numbers[62:93]) < 2:
        return None
    else:
        min_num1 = min(numbers[62:93])
        numbers[:] = (value for value in numbers if value != min_num1)
        min_num2 = min(numbers[62:93])
        return min_num2