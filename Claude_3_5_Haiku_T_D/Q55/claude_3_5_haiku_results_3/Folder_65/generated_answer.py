def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [lst[i % n] for i in range(start, end + 1)]
            if len(sublist) <= n and calculate_product(sublist) == 46:
                result.append(sublist)
    return result

def calculate_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product