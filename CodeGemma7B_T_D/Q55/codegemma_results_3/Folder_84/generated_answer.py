from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    number_product = 906
    sublists = []
    for indices in combinations_with_replacement(range(len(circular_list)), r=1):
        sublist = [circular_list[index] for index in indices]
        product = 1
        for number in sublist:
            product *= number
        if product == number_product:
            sublists.append(sublist)
    return sublists