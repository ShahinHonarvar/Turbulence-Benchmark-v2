def find_n_th_smallest_num(numbers):
    numbers.sort()
    if len(numbers) < 4:
        return None
    return numbers[3]