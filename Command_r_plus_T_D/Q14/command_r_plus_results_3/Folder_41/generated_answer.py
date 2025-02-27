def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        second_smallest = None
        smallest = numbers[4]
        for num in numbers[4:]:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif second_smallest is None or (num < second_smallest and num != smallest):
                second_smallest = num
        return second_smallest