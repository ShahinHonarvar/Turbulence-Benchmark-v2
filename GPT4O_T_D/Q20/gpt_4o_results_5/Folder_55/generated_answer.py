def find_n_th_smallest_num(numbers):
    if len(numbers) < 13:
        return None
    numbers.sort()
    return numbers[12]