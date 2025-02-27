def lists_with_product_equal_n(circular_list):
    product_dict = {}
    for i, num in enumerate(circular_list):
        product_dict.setdefault(num, []).append(i)
    if not set(product_dict.keys()).issubset({0, 1, 2, 4, 6, 8, 12, 24, 48}):
        return []
    result_list = []
    for product in product_dict.keys():
        if product * 2 > len(circular_list) and product != 1 and (product != 48):
            continue
        for idx in product_dict[product]:
            result_list.append(circular_list[idx])
            start_idx = idx
            count = len(circular_list)
            while True:
                product *= circular_list[(idx + count) % len(circular_list)]
                count += 1
                if product > 48:
                    break
                if product == 48:
                    result_list.append(circular_list[(idx + count) % len(circular_list)])
                    count += 1
                    continue
                if count > idx:
                    break
                product_dict.setdefault(product, []).append((idx + count) % len(circular_list))
    return result_list