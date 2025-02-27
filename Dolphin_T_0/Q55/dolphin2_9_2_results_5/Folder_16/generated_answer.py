def lists_with_product_equal_n(circular_list, n):

    def get_sublists_with_product_equal_n(sublist, index_map, n):
        length = len(sublist)
        if length > 1 and sublist[0] * sublist[-1] != n:
            return []
        if length == len(circular_list) and sublist[0] * sublist[-1] == n:
            return [sublist]
        result = []
        next_map = index_map.copy()
        for k in range(1, length + 1):
            next_map[length - k + index_map[-1]] = length - k
            result += get_sublists_with_product_equal_n(sublist[:-k] + sublist[-1:], next_map, n)
        return result
    sublist = []
    index_map = list(range(len(circular_list)))
    for _ in range(len(circular_list)):
        sublist.append(circular_list[index_map.pop(0)])
    return get_sublists_with_product_equal_n(sublist, index_map, n)