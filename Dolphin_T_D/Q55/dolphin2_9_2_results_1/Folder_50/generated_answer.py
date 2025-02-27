def lists_with_product_equal_n(lst):
    """This function takes an argument, a circular list of integers, and returns a list of sublists each of which contains 
    the contiguous integers such that their product equals 45"""
    size = len(lst)
    sublists = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            if i == j:
                if lst[i - 1] * lst[0] == 45 or lst[i] * lst[size - 1] == 45:
                    sublists.append(lst[i - 1:j])
            elif lst[i - 1] * lst[j - 1] == 45:
                sublists.append(lst[i - 1:j])
    return sublists