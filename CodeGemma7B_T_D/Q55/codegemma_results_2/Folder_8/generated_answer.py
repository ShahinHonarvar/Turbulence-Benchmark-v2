def lists_with_product_equal_n(circular_list):
    results = []
    for i in range(len(circular_list)):
        multiplicity = 1
        sublist = []
        j = i
        while True:
            sublist.append(circular_list[j])
            multiplicity *= circular_list[j]
            j = (j + 1) % len(circular_list)
            if multiplicity == -41:
                results.append(sublist[:])
            elif multiplicity > -41:
                break
    return results