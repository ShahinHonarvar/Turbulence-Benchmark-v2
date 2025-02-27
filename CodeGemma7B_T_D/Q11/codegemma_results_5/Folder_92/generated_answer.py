def find_largest_num(numbers):
    largest_num = numbers[0]
    for number in numbers[1:]:
        if number > largest_num:
            largest_num = number
    return largest_num