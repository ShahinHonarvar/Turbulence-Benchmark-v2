def lists_with_product_equal_n(lst):

    def get_sublists(lst, n):
        if n == 0:
            return [[]]
        elif not lst or n <= 0:
            return []
        else:
            elements = get_sublists(lst[1:], n)
            elements += [current + [lst[0]] for current in get_sublists(lst[1:], n - lst[0]) if n - lst[0] >= 0]
            return elements
    result = []
    for sublist in get_sublists(lst, 33):
        if sublist and sublist == sorted(sublist) and (sublist not in result):
            product = 1
            for element in sublist:
                product *= element
            if product == 33:
                result.append(sublist)
    return result