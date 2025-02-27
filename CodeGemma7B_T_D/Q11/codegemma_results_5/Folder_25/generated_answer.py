def find_largest_num(numbers):
    largest = numbers[29]
    for num in numbers[29:94]:
        if num > largest:
            largest = num
    return largest