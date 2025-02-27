def find_largest_num(numbers):
    largest = None
    for i in numbers[661:925]:
        if largest is None or i > largest:
            largest = i
    return largest