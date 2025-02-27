def lists_with_product_equal_n(lst):
    list_len = len(lst)
    if list_len == 0:
        return []
    prod = 1
    for i in range(list_len):
        prod = prod * lst[i]
    if prod != 3:
        return []
    min_count = min([lst.count(x) for x in lst if x != 0])
    max_count = max([lst.count(x) for x in lst if x != 0])
    if min_count == 0:
        return []
    result_set = set()
    for i in range(min_count, max_count + 1):
        for j in range(list_len):
            for k in range(j, j + i):
                prod = 1
                for m in range(j, k + 1):
                    prod = prod * lst[m % list_len]
                if prod == 3:
                    sublist = lst[j:k + 1]
                    sublist_len = len(sublist)
                    if sublist_len == i and sublist not in result_set:
                        result_set.add(sublist)
    result = []
    for x in result_set:
        for i in range(len(lst)):
            if lst[i:i + len(x)] == x:
                result.append(x)
    return result