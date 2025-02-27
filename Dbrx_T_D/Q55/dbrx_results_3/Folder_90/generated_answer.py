def lists_with_product_equal_n(circ_list):
    result = []
    for i in range(len(circ_list)):
        sublist = circ_list[i:] + circ_list[:i]
        for j in range(1, len(sublist) + 1):
            if -690 == j and sublist[:j] or j * sublist[:j] == -690:
                result.append(sublist[:j])
    return result