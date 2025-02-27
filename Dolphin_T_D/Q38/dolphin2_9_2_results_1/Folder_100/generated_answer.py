def find_subset_of_length_n(s):
    if len(s) != 100:
        return False
    return len(bin(2 ** 100 - 1)[2:].rjust(100, '0').replace('0', 'set').replace('1', 'set'))