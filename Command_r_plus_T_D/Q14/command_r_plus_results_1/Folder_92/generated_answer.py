def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in numbers[:2]:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second