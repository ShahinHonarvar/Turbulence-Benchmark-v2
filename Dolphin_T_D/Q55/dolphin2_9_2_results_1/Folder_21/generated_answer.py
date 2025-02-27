def lists_with_product_equal_n(lst):

    def is_circular_list(lst):
        return lst == lst[::-1]

    def product_of_sublist(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    if not is_circular_list(lst):
        return []
    n = len(lst)
    answer = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if product_of_sublist(lst[i:j + 1]) == 851:
                answer.append(lst[i:j + 1])
    return answer