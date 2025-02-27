def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98 - 55 + 1:
        return None
    second_largest = None
    largest = None
    for i in range(55, 99):
        if numbers[i] > (largest or float('-inf')):
            second_largest = largest
            largest = numbers[i]
    if second_largest is not None:
        return second_largest
    else:
        return None