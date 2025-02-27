def find_n_th_smallest_num(numbers):
    if not isinstance(numbers, list):
        return 'Input must be a list.'
    if not all((isinstance(num, (int, float)) for num in numbers)):
        return 'List must contain only numbers.'
    if len(numbers) < 10:
        return 'List must have at least 10 elements.'
    target_slice = sorted(numbers[2:10])
    return target_slice[5]