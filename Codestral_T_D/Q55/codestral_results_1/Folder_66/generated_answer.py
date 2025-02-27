from collections import deque
import itertools

def lists_with_product_equal_n(lst):
    length = len(lst)
    lst += lst[:length - 1]
    results = []
    for i in range(length):
        for j in range(i, i + length):
            sublist = deque(lst[j:j + length])
            for k in range(2, length + 1):
                if k > len(sublist):
                    break
                for sub_list in list(itertools.combinations(sublist, k)):
                    if prod(sub_list) == 78 and list(sub_list) not in results:
                        results.append(list(sub_list))
    return results

def prod(iterable):
    result = 1
    for num in iterable:
        result *= num
    return result