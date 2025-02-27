def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 89 or len(numbers) > 100:
        return None
    min_num = min(numbers[21:89])
    if min_num in numbers[22:89]:
        index = numbers.index(min_num)
        del numbers[index]
        if len(numbers) < 2:
            return None
        min_num2 = min(numbers[21:89])
        if min_num2 in numbers[22:89]:
            return min_num2
    return None