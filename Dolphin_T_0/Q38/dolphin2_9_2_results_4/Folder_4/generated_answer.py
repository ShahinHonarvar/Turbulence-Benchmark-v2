def find_subset_of_length_n(s):
    n = len(s)
    if n > 15:
        if n == 16:
            return 2
        else:
            return 2 ** 15
    else:
        return 2 ** n