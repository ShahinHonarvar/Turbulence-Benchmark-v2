def sum_odd_ints_inclusive(integer_list):
    start_index = 59
    end_index = 97
    if len(integer_list) < end_index + 1:
        raise IndexError('The list is not long enough to include the specified index range.')
    odd_ints = [i for i in integer_list[start_index:end_index + 1] if i % 2 != 0]
    if not odd_ints:
        return 0
    return sum(odd_ints)