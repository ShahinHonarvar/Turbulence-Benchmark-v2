def lists_with_product_equal_n(lst):

    def get_sublists(lst, product):
        sublists = []
        n = len(lst)
        for i in range(n):
            product_now = 1
            for j in range(i, i + n):
                product_now *= lst[j % n]
                if product_now == product:
                    sublist = lst[i:j + 1]
                    sublists.append(sublist)
                if product_now > product:
                    break
        return sublists
    n = len(lst)
    sublist_of_n = get_sublists(lst + lst, 96)
    output = []
    for sublist in sublist_of_n:
        sublist_set = set(sublist)
        output.append(list(sublist_set))
    return output if len(output) else []