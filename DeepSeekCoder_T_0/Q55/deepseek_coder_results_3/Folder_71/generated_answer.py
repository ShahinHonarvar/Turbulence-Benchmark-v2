def lists_with_product_equal_n(circular_list):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p

    def find_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            for end in range(start + 1, len(lst) + start + 1):
                sublist = lst[start:end] if end <= len(lst) else lst[start:] + lst[:end - len(lst)]
                if product(sublist) == 47:
                    sublists.append(sublist)
        return sublists
    return find_sublists(circular_list)