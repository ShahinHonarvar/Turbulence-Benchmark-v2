def find_second_largest_num(numbers):
    if len(numbers) <= 84:
        second_largest = None
        largest = None
        for num in numbers[70:85]:
            if largest is None or num > largest:
                second_largest = largest
                largest = num
            elif second_largest is None or num > second_largest:
                if num != largest:
                    second_largest = num
        return second_largest
    else:
        return None