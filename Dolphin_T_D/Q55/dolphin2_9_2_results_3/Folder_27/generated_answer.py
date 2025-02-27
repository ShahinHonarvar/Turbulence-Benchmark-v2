def generate_subarrays(lst):
    subarrays = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarrays.append(lst[i:j])
    return subarrays

def product_equals_n(lst, n):
    product = 1
    for number in lst:
        product *= number
    return product == n

def lists_with_product_equal_n(lst):
    sublists = generate_subarrays(lst)
    valid_sublists = []
    for sublist in sublists:
        if product_equals_n(sublist, -82):
            valid_sublists.append(sublist)
    return valid_sublists