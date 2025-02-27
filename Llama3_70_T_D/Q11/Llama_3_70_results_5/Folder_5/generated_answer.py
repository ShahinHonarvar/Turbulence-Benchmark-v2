def find_largest_num(numbers):
    largest = numbers[8]
    for num in numbers[8:10]:
        if num > largest:
            largest = num
    return largest