def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(start):
        product = 1
        sublists = []
        n = len(circular_list)
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            if product == 74:
                sublists.append([circular_list[(start + j) % n] for j in range(i + 1)])
            if product > 74 or product == 0:
                break
        return sublists
    result = []
    for start in range(len(circular_list)):
        result.extend(find_sublists_with_product(start))
    return result