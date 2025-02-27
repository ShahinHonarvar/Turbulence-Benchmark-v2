def find_n_th_smallest_num(numbers):
    numbers = list(numbers)
    if len(numbers) < 578:
        return None
    numbers = numbers[365:579]
    numbers.sort()
    return numbers[16]