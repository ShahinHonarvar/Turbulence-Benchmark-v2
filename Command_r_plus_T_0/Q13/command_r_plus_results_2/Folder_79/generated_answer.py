def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        numbers_slice = numbers[4:]
        second_largest = None
        largest = max(numbers_slice)
        for num in numbers_slice:
            if num < largest:
                if second_largest is None or num > second_largest:
                    second_largest = num
        return second_largest