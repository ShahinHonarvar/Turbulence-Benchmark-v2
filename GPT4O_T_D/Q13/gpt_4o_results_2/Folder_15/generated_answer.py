def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    first_largest = second_largest = float('-inf')
    for number in numbers[:4]:
        if number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif number > second_largest:
            second_largest = number
    return second_largest if second_largest != float('-inf') else None