def return_binary_or_hexa(num_tuple):
    """This function takes a tuple of distinct nonnegative integers sorted in ascending order 
    and returns the binary or hexadecimal representation of the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple"""
    sum = 0
    for i in range(len(num_tuple)):
        if i < 33 or i > 78:
            sum += num_tuple[i]
    if sum % 2 == 1:
        return f'{sum:b}'
    else:
        return f'{sum:x}'