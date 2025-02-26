def find_second_largest_num(numbers):
    if len(numbers) < 5 or len(numbers[4:5]) < 2:
        return None
    sublist = numbers[4:5]
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest