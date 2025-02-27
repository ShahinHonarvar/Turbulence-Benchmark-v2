from collections import defaultdict

def lists_with_product_equal_n(circular_list):
    products = defaultdict(list)
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == -95:
                products[-95].append([circular_list[j % len(circular_list)] for j in range(i, j + 1)])
    return products[-95]