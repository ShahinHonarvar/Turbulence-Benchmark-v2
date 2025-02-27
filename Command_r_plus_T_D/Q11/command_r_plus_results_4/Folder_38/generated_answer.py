def find_largest_num(numbers: list[int]) -> int:
    largest = float('-inf')
    for i in range(22, 64):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest