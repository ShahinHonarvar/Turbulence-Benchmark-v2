def find_largest_num(numbers: list[int]) -> int:
    largest_num = float('-inf')
    for num in numbers[22:64]:
        if num > largest_num:
            largest_num = num
    return largest_num