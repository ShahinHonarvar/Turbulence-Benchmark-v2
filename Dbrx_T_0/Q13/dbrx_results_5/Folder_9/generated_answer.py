def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 200 < 2:
        return None
    first, second = (max(numbers[:201]), None)
    for num in numbers[:201]:
        if num < first:
            if not second or num > second:
                second = num
    for num in numbers[201:]:
        if first < num < second:
            second = num
    return second