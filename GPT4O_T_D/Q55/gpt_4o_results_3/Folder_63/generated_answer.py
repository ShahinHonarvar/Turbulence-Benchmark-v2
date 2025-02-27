def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(start):
        product = 1
        sublist = []
        for i in range(len(circular_list)):
            index = (start + i) % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == 96:
                sublists.append(sublist.copy())
            if product > 96 or len(sublist) == len(circular_list):
                break
    sublists = []
    for start in range(len(circular_list)):
        find_sublists_with_product(start)
    return sublists