from itertools import islice

def lists_with_product_equal_n(circ_list):
    k = 1
    results = []
    for idx in range(len(circ_list)):
        for jdx in range(idx, len(circ_list)):
            curr_results = get_sublist_product_equal_n(circ_list[idx:jdx + 1], k)
            if curr_results:
                results.extend(curr_results)
    return results

def get_sublist_product_equal_n(curr_list, k):
    if len(curr_list) <= k:
        result = [curr_list]
    else:
        sublists = get_sublists_of_len(curr_list, k)
        result = [sublist for sublist in sublists if sublist]
    return result

def get_sublists_of_len(curr_list, length):
    result = []
    for idx in range(len(curr_list) - length + 1):
        sublist = list(islice(curr_list, idx, idx + length))
        result.append(sublist)
    return result