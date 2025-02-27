def lists_with_product_equal_n(circular_list):
    seen = set()
    for idx, n in enumerate(circular_list):
        product = n
        sublist = [n]
        i = idx + 1
        while i <= len(circular_list) - 1:
            next_element = circular_list[i]
            product *= next_element
            sublist.append(next_element)
            if product == -91:
                joined = ''.join((str(i) for i in sublist))
                seen.add(joined)
            i += 1
    return list(seen)