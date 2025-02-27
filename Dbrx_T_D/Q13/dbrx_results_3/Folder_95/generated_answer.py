def find_second_largest_num(numbers):
    if not isinstance(numbers, list) or len(numbers) <= 1:
        return None
    second_largest = None
    for num in numbers[82:87]:
        if not second_largest and num > min(numbers[:index]) or (second_largest and num > second_largest and (num < max(numbers[:index]))):
            second_largest = num
            index = numbers.index(num) + 1
        elif num == second_largest:
            index = numbers.index(num, index)
    if second_largest is not None and second_largest < max(numbers[:82]):
        return second_largest
    return None