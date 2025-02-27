def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        second_largest = max(numbers[8:10])
        for num in numbers[8:10]:
            if num != second_largest:
                return num
        return None