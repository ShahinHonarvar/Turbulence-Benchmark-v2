from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(n, iterable):
        for i in range(len(iterable)):
            subarray = list(islice(cycle(iterable), i, i + len(iterable)))
            if subarray[i:] == subarray[:i]:
                subarray = subarray[i:] + subarray[:i]
            if subarray[0] * subarray[1:] == n:
                yield subarray[1:]
    return list(set(sublists_with_product_equal_n(-26, circular_list)))