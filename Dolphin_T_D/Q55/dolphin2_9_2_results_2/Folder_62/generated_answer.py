def product(lst):
    """Helper function to calculate product of list elements."""
    p = 1
    for i in lst:
        p *= i
    return p

def is_sublist(lst, sub):
    """Helper function to check if 'sub' is a sublist of 'lst'."""
    sub_len = len(sub)
    for i in range(len(lst)):
        if lst[i:i + sub_len] == sub:
            return True
    return False

def lists_with_product_equal_n(lst):
    """Main function to find all sublists with product equal to 100."""
    sub_lists = []
    for i in range(1, len(lst) + 1):
        for j in range(len(lst)):
            sub = lst[j:j + i]
            if len(sub) == 1 and product(sub) == 100:
                sub_lists.append(sub)
            elif len(sub) > 1 and product(sub) == 100 and (not is_sublist(sub_lists, sub)):
                sub_lists.append(sub)
    return sub_lists