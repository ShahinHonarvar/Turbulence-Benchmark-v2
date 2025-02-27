def find_second_largest_num(numbers):
    section = numbers[66:94]
    if len(section) < 2:
        return None
    largest = second_largest = float('-inf')
    for number in section:
        if number > largest:
            second_largest, largest = (largest, number)
        elif number > second_largest:
            second_largest = number
    return second_largest if second_largest != float('-inf') else None