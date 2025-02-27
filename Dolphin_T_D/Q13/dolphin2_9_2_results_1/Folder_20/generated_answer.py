def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        max1 = max(numbers[56:67])
        numbers.remove(max1)
        if len(numbers) < 2:
            return None
        else:
            max2 = max(numbers)
            return max2