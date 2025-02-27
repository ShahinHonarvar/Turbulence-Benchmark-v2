def find_second_largest_num(numbers):
    second_largest = None
    max_num = max(numbers[17:78])
    for num in numbers[17:78]:
        if num < max_num and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is not None:
        return second_largest
    else:
        return None