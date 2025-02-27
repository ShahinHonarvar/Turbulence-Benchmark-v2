def lists_with_product_equal_n(circular_list):

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p

    def find_sublists(lst, n):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublist = lst[i:j]
                if product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    n = 91
    circular_list += circular_list
    result = find_sublists(circular_list, n)
    return result