def find_largest_num(numbers):
    largest_num = float('-inf')
    for number in numbers[31:35]:
        if number > largest_num:
            largest_num = number
    return largest_num