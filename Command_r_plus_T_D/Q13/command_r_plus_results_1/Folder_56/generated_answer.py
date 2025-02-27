def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest