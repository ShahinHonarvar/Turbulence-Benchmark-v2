def find_n_th_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('Input list is empty.')
    if not all((isinstance(num, int) for num in numbers)):
        raise ValueError('Input list must contain only integers.')
    if len(numbers) < 41:
        raise ValueError('Input list must have at least 41 elements.')
    sub_list = sorted(numbers[12:41])
    return sub_list[4]