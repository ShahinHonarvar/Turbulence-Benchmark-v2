def find_largest_num(numbers):
    largest = numbers[32]
    for num in numbers[33:36]:
        if num > largest:
            largest = num
    return largest