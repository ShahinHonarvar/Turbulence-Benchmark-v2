def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        numbers_slice = numbers[4:]
        second_smallest = min(numbers_slice)
        for num in numbers_slice:
            if num < second_smallest and num > min(numbers):
                second_smallest = num
        return second_smallest