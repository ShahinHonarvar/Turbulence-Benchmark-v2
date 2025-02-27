def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(lst):
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublists.append(lst[i:j])
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                sublists.append(lst[i:] + lst[:j])
        return sublists
    sublists = get_sublists(circular_list)
    result = [sublist for sublist in sublists if product(sublist) == -8]
    return result