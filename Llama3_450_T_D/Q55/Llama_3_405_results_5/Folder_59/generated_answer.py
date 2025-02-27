def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(circular_list):
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + 1):
                sublists.append(circular_list[i:j])
            for j in range(i):
                sublists.append(circular_list[i:] + circular_list[:j])
        return sublists
    return [sublist for sublist in get_sublists(circular_list) if product(sublist) == -3]