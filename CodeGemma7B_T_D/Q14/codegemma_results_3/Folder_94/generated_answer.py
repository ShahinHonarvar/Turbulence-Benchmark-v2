def find_second_smallest_num(numbers):
    if not numbers or index_first < 0 or index_last > len(numbers) - 1:
        return None
    numbers.sort()
    return numbers[index_first + 1]