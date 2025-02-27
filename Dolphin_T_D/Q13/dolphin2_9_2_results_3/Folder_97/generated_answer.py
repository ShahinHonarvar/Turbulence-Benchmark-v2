def find_second_largest_num(numbers):
    sublist = numbers[40:81]
    if not sublist:
        return None
    largest = second_largest = None
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest