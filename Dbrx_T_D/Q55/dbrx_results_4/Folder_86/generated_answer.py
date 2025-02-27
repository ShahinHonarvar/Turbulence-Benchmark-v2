from itertools import islice

def circular_list_product(lst, start=0):
    result = 1
    for i in range(start, start + len(lst)):
        j = i % len(lst)
        result *= lst[j]
    return result

def lists_with_product_equal_n(lst, n):
    if not lst:
        return []
    result = []
    for i in range(len(lst)):
        current_product = 1
        for j in range(i, len(lst)):
            current_product *= lst[j]
            if current_product == n:
                result.append(lst[i:j + 1])
                break
            elif current_product < n:
                continue
            else:
                break
    return result