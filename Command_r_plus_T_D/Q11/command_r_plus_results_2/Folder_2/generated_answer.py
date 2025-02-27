def find_largest_num(numbers: list[int]) -> int:
    largest_num = float('-inf')
    for i in range(15, 40):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num