def find_largest_num(numbers):
    subset = numbers[70:85]
    largest = subset[0]
    for num in subset:
        if num > largest:
            largest = num
    return largest