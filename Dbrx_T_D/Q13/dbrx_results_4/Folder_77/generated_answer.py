def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 538 - 527:
        return None
    else:
        second_largest = None
        largest = None
        for num in numbers[527:539]:
            if largest is None or num > largest:
                second_largest = largest
                largest = num
            elif num < largest and (second_largest is None or num > second_largest):
                second_largest = num
        return second_largest