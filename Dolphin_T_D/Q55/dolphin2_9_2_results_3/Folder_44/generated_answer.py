def circular_list_to_simple(lst):
    n = len(lst)
    return lst + lst[:n // 2]

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = circular_list_to_simple(lst)
    result = []
    product = 1
    for i in range(n):
        product *= lst[i]
        for j in range(i + 1, n + 1):
            if product // lst[j - 1] == 29:
                result.append(lst[i:j])
                product //= lst[j - 1]
    return result