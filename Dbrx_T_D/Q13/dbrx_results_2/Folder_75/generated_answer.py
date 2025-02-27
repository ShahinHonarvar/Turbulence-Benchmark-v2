def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:57]), None)
    for num in numbers[:57]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second