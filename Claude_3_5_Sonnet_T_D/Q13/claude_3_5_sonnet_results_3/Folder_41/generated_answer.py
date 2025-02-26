def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        subset = numbers[6:7]
        if len(subset) < 2:
            return None
        else:
            return sorted(subset)[-2]