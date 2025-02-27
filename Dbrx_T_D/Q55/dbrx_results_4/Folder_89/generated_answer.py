from itertools import islice

def circular_slice(lst, start, end):
    """Yields a circular slice of the list."""
    length = len(lst)
    for i in range(start, end + 1):
        yield lst[i % length]

def is_product_equal_n(lst, n):
    """Checks if the product of the elements in the list is equal to n."""
    prod = 1
    for num in lst:
        prod *= num
        if prod > n:
            return False
        if prod == n:
            return True
    return False

def lists_with_product_equal_n(lst):
    """Returns a list of sublists with product equal to 57."""
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublst = list(circular_slice(lst, i, j))
            if is_product_equal_n(sublst, 57):
                result.append(sublst)
    return result