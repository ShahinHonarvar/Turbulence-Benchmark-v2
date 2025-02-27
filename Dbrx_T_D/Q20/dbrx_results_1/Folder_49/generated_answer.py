def find_n_th_smallest_num(numbers):
    if len(numbers) < 200:
        raise ValueError('Input list should have at least 200 elements')
    numbers = numbers[20:201]
    numbers.sort()
    return numbers[10]