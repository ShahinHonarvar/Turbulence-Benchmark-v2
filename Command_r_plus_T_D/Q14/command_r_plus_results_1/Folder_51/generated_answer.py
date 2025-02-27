def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = min(numbers[1:9])
    for num in numbers[1:9]:
        if num != smallest:
            second_smallest = num
            break
    return second_smallest