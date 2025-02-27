from itertools import chain, islice

def lists_with_product_equal_n(circular_list):
    max_size = len(circular_list)
    for size in range(1, max_size + 1):
        for start in range(max_size):
            sublist = list(islice(circular_list, start, start + size))
            if len(sublist) < size or sublist[0] * sublist[-1] != -1:
                continue
            if len(sublist) == size:
                circular_list.append(sublist.pop(0))
            yield sublist
    circular_list.extend(chain.from_iterable(zip(*circular_list)))