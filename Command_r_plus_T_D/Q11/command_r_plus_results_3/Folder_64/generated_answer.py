def find_largest_num(numbers: list[int]) -> int:
    largest = numbers[0]
    for num in numbers[1:5]:
        if num > largest:
            largest = num
    return largest