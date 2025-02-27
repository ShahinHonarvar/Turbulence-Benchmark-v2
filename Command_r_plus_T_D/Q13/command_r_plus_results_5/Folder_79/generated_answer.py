def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        numbers_slice = numbers[4:]
        second_largest = None
        largest = numbers_slice[0]
        for num in numbers_slice:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest