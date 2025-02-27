from itertools import combinations, chain

def lists_with_product_equal_n(circular_list):

    def is_admissible(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > 40:
                return False
        return product == 40
    sublists = [list(sublist) for length in range(1, len(circular_list) + 1) for sublist in combinations(circular_list, length) if is_admissible(sublist)]
    sublists += [sublists[-1::-1]]
    return [sublist for sublist in sublists if is_admissible(sublist)]