from itertools import islice, cycle

def circular_list(iterable):
    itered = iter(iterable)
    *others, head, tail = itered
    return (*others, head, tail)

def find_sublists_with_product_equal_n(n, circular_list):
    result = []
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        subproduct = sublist[0]
        for j in range(i + 1, i + len(circular_list)):
            sublist.append(circular_list[j])
            subproduct *= circular_list[j]
            if subproduct == n:
                result.append(sublist[:])
                break
            if subproduct > n:
                break
    return result

def lists_with_product_equal_n(n, input_list):
    circular_list = circular_list(input_list)
    return find_sublists_with_product_equal_n(n, circular_list)