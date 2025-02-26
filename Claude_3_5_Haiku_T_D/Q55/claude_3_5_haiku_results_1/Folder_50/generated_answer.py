def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [circular_list[(start + i) % n] for i in range(end - start + 1)]
            if product(sublist) == 45:
                result.append(sublist)
    return result

def product(lst):
    p = 1
    for num in lst:
        p *= num
    return p