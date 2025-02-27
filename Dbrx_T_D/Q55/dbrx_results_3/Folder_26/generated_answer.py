from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def circular_sublists(sublist):
        result = []
        for i in range(len(sublist)):
            result.append(sublist[i:] + sublist[:i])
        return result

    def product_of_sublist(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    possible_sublists = [sl for sl in circular_sublists(circular_list) if product_of_sublist(sl) == 93]
    unique_sublists = [list(sublist) for sublist in {tuple(sublist) for sublist in possible_sublists}]
    return unique_sublists