def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = min(numbers[1:9])
    for num in numbers[1:9]:
        if num > smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num
    return second_smallest