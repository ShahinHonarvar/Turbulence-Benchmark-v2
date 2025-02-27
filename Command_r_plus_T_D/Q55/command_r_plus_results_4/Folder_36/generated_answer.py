def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def find_sublists(lst, target_product):
        length = len(lst)
        for size in range(1, length + 1):
            for start in range(0, length):
                sublist = lst[start:start + size]
                if product(sublist) == target_product:
                    yield sublist
    return list(find_sublists(circular_list, 714))