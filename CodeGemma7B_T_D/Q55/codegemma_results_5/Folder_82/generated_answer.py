def lists_with_product_equal_n(circular_list):
    end = len(circular_list)
    for i in range(end):
        product = circular_list[i]
        items = [circular_list[i]]
        for j in range(i + 1, end):
            product *= circular_list[j]
            items.append(circular_list[j])
            if product == 8:
                yield items
            if product > 8:
                break
        circular_list.append(circular_list.pop(0))