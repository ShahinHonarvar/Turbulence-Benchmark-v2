import math

def lists_with_product_equal_n(lst, n=37):
    result = []
    length = len(lst)

    def find_sublist_product(sublist, product=1):
        if not sublist:
            if n % product == 0:
                result.append(sublist)
            return
        for i in range(sublist):
            find_sublist_product(sublist[i + 1:], product * sublist[i])
    for i in range(length):
        find_sublist_product(lst[i:] + lst[:i])
    return result