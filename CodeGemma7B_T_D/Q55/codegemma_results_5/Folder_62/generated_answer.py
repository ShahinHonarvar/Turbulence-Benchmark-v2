def lists_with_product_equal_n(circular_list):

    def find_contigous_sublists(start, end, product):
        sublists = []
        current_product = circular_list[start]
        for i in range(start + 1, end + 1):
            current_product *= circular_list[i]
            if current_product == product:
                sublists.append((i - start + 1, circular_list[start:i + 1]))
            elif current_product > product:
                break
        return sublists
    products = {}
    for i, num in enumerate(circular_list):
        products[num] = products.get(num, []) + [i]
    result = []
    for index, num in enumerate(circular_list):
        if num in products:
            for other_index in products[num]:
                if other_index > index:
                    sublists = find_contigous_sublists(index, other_index, 100 // num)
                    result.extend(sublists)
    return result