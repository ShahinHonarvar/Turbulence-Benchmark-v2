def find_n_th_smallest_num(numbers):
    if len(numbers) < 100 or len(numbers) > 1000:
        raise ValueError('Input list must have between 100 and 1000 elements')
    sub_list = numbers[84:100]
    sub_list.sort()
    if len(sub_list) < 7:
        raise ValueError('Not enough distinct numbers in the specified range')
    return sub_list[6]