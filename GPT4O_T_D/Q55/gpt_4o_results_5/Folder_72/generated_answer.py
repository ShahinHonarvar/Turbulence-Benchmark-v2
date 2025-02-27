from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = 10
    size = len(circular_list)
    results = []
    circular = circular_list + circular_list[:-1]
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular[end]
            if product == n:
                results.append(circular[start:end + 1])
            if product == 0 or product > n:
                break
    return results