def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_two(start_idx):
        product = 1
        sublist = []
        results = []
        for i in range(len(circular_list)):
            idx = (start_idx + i) % len(circular_list)
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product == 2:
                results.append(sublist[:])
            if product == 0:
                break
            if product > 2 or (product > 0.5 and idx == start_idx - 1):
                break
        return results
    results = []
    for i in range(len(circular_list)):
        results.extend(find_sublists_with_product_two(i))
    return results