def get_all_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists

def product_of_list(lst):
    product_value = 1
    for i in lst:
        product_value *= i
    return product_value

def lists_with_product_equal_n(lst):
    sublists = get_all_sublists(lst)
    result = [lst for lst in sublists if product_of_list(lst) == -65]
    return result