def lists_with_product_equal_n(lst):

    def find_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            product = 1
            for j in range(len(lst)):
                product *= lst[(i + j) % len(lst)]
                if product == -69:
                    sublists.append(lst[(i + j) % len(lst):i + (j + 1) % len(lst)])
                    if j + 1 != len(lst):
                        sublists.append(lst[i:i + j + 1])
        return sublists
    sublists = find_sublists(lst)
    return sublists