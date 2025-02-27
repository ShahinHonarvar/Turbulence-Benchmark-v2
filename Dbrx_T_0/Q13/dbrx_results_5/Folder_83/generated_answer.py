def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 90 < 2:
        return None
    first, second = (max(numbers[90:91]), None)
    for num in numbers[90:91]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    for num in numbers[:90]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second