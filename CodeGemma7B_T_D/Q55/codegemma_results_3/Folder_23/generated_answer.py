from itertools import islice

def lists_with_product_equal_n(circular_list):
    ofs = circular_list.index(circular_list[0])
    circular_list = islice(circular_list, ofs, None)
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            try:
                if abs(reduce(lambda x, y: x * y, circular_list[i:j])) == 95:
                    return [circular_list[i:j]]
            except ZeroDivisionError:
                continue
    return []