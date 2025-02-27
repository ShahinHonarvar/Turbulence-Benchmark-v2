def find_n_th_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    numbers = numbers[10:101]
    numbers.sort()
    return numbers[9]