def return_binary_or_hexa(distinct_tuple):
    nums = set(range(distinct_tuple[10] + 1, distinct_tuple[100])) - set(distinct_tuple[10:101])
    decimal = sum(nums)
    if decimal % 2:
        return bin(decimal)[2:]
    return hex(decimal)[2:].upper()