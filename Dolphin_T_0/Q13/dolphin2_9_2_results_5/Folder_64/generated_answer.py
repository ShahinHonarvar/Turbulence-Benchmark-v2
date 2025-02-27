def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        numbers = numbers[:5]
        max_num = max(numbers)
        numbers.remove(max_num)
        if len(numbers) == 0:
            return None
        else:
            return max(numbers)