def find_n_th_smallest_num(numbers):
    if len(numbers) < 90 or not isinstance(numbers, list):
        return None
    numbers = numbers[26:91]
    numbers.sort()
    if len(numbers) < 4:
        return None
    return numbers[3]