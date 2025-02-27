def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[:15][70:], key=numbers.count), None)
    for num in numbers[:15][70:]:
        if num == first:
            continue
        if second is None or num > second:
            second = num
        if second is not None and second > first:
            break
    return second