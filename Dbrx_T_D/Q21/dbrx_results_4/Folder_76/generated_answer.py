def all_ints_div_by_num(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    div_by_901 = [num for num in lst[600:699] if isinstance(num, int) and num % 901 == 0]
    return div_by_901