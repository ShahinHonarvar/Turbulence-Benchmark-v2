def return_binary_or_hexa(x: tuple[int, int, int, int, int, int, int]) -> str:
    """
    returns the binary or hexadecimal representation of the sum of all integers from a+1 to b-1 (both inclusive)
    that are not present in the tuple.
    """
    max_num = x[7]
    min_num = x[2]
    sum = 0
    for num in range(min_num + 1, max_num):
        if num not in x:
            sum += num
    if sum % 2 > 0:
        result = bin(sum)[2:]
    else:
        result = hex(sum)[2:].lower()
    return result