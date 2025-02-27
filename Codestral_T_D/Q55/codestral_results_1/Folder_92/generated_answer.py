from itertools import cycle

def lists_with_product_equal_n(lst):

    def find_sublists(lst, target_product):
        sublists = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst) + i):
                product *= lst[j % len(lst)]
                if product == target_product:
                    sublists.append(lst[i:j + 1])
                if product > target_product:
                    break
        return sublists
    sublists = find_sublists(lst, 5)
    return sublists