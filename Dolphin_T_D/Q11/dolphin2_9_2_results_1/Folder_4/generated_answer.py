def find_largest_num(numbers):
    largest = float('-inf')
    for num in numbers[12:93]:
        if num > largest:
            largest = num
    return largest