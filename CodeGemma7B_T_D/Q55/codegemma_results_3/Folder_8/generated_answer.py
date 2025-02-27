def lists_with_product_equal_n(circular_list):
    """
    Your Python code should go here.
    """
    results = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            if product * circular_list[j] == -41 and len(sublist) < len(circular_list):
                sublist.append(circular_list[j])
                product *= circular_list[j]
            elif product * circular_list[j] != -41 or len(sublist) >= len(circular_list):
                break
        if product == -41 and len(sublist) <= len(circular_list):
            results.append(sublist)
        circular_list = circular_list[1:] + [circular_list[0]]
    return results