def lists_with_product_equal_n(lst):

    def circular_substring(lst):
        if len(lst) < 2:
            return lst
        for i in range(len(lst)):
            for length in range(2, len(lst) + 1):
                if i + length <= len(lst):
                    yield lst[i:i + length]
                else:
                    yield (lst[i:] + lst[:length - (len(lst) - i) + 1])
    result = []
    for sublist in circular_substring(lst):
        if sublist != [] and sublist != lst:
            if round(prod(sublist)) == 632:
                result.append(sublist)
    return result

def prod(lst):
    product = 1
    for i in lst:
        product *= i
    return product