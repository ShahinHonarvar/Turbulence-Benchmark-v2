from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = 93
    size = len(circular_list)
    circular_list += circular_list
    sublists = []
    for i in range(size):
        for j in range(i, i + size):
            for k in range(j - i + 1, 0, -1):
                sub_list = circular_list[j - k + 1:j + 1]
                product = 1
                for num in sub_list:
                    product *= num
                if product == n:
                    sublists.append(sub_list)
    return sublists