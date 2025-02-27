def find_second_smallest_num(numbers):
    numbers.sort()
    return numbers[75:89][1] if len(numbers[75:89]) >= 2 else 'None'