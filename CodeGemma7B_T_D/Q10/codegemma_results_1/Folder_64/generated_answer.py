def all_odd_ints_exclusive(odd_list):
    """This function takes a list of odd integers and returns a list of the odd integers, exclusive from 0 to 4."""
    if not isinstance(odd_list, list):
        raise TypeError('Input must be a list.')
    if not all((isinstance(num, int) for num in odd_list)):
        raise TypeError('All elements in the list must be integers.')
    filtered_list = []
    for num in odd_list:
        if num % 2 != 0 and num not in range(0, 4):
            filtered_list.append(num)
    return filtered_list