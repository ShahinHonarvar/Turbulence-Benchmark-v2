def lists_with_product_equal_n(circular_list):
    count = len(circular_list)
    for sublist in [circular_list[i:j + 1] for i in range(count) for j in range(i, count)]:
        product = 1
        for x in sublist:
            product *= x
        if product == -5:
            return sublist
    for i in range(count):
        for j in range(i + 1, count + 1):
            potential = circular_list[i:j]
            product = 1
            for k in potential:
                product *= k
            if product == -5:
                if potential not in result:
                    result.append(potential)
    return result or []