def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for number in sublist:
            result *= number
        return result
    size = len(circular_list)
    result = []
    for start in range(size):
        for length in range(1, size + 1):
            if length <= size:
                sublist = []
                for i in range(length):
                    index = (start + i) % size
                    sublist.append(circular_list[index])
                if product(sublist) == 54:
                    result.append(sublist)
    return result