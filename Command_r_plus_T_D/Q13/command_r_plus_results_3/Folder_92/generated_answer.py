def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return None
    second_largest = None
    for num in numbers[:2]:
        if num is not None:
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest