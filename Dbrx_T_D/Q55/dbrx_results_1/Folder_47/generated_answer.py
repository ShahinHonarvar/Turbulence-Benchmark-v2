from itertools import combinations

def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def is_circular_sublist(sublist):
        sublen = len(sublist)
        for i in range(sublen):
            if product(sublist[i:i + sublen]) == -94:
                return True
        return False
    return [sublist for sublist in combinations(lst, max(1, len(lst))) if is_circular_sublist(sublist) and product(sublist) == -94]