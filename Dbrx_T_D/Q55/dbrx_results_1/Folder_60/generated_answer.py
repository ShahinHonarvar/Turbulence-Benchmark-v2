from itertools import islice

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(lst, n):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if n < 0 or (n == 0 and (not lst[j])):
                    break
                n -= lst[j]
                if n == 0:
                    result.append(lst[i:j + 1])
            n += lst[i]
        return result
    if not circular_list:
        return []
    n = 49
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            if n < 0 or (n == 0 and (not circular_list[j])):
                break
            n -= circular_list[j]
            if n == 0:
                return sublists_with_product_equal_n(circular_list[i:j + 1], n)
        n += circular_list[i]
    for i in range(len(circular_list)):
        n = 49
        for j in range(i, len(circular_list)):
            if n < 0 or (n == 0 and (not circular_list[j])):
                break
            n -= circular_list[j]
            if n == 0:
                return sublists_with_product_equal_n(circular_list[j:i + 1][::-1], n)
        n += circular_list[i]
    return []