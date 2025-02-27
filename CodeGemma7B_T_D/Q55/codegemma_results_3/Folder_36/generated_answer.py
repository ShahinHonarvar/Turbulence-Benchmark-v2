from itertools import islice

def circular_product(circular_list):
    """Calculates the product of a circular list."""
    return circular_list[-1] * circular_list[0] * circular_list[1]

def find_sublists_with_product_n(circular_list, n):
    """Finds sublists with the product of the elements equal to n."""
    sublists = []
    current_sublist = []
    current_product = 1
    for i, element in enumerate(circular_list):
        current_sublist.append(element)
        current_product *= element
        while current_product > n and current_sublist:
            current_product //= current_sublist.pop(0)
        if current_product == n:
            sublists.append(current_sublist.copy())
        if i == len(circular_list) - 1 and current_sublist and (circular_product(circular_list[i:] + circular_list[:i]) == n):
            sublists.append(circular_list[i:] + circular_list[:i])
    return sublists