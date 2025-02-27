def lists_with_product_equal_n(circular_list):

    def will_wrap(index, list_size):
        return (index + 1) % list_size == (index - 1 + list_size) % list_size

    def product(sublist):
        product = 1
        for element in sublist:
            product *= element
        return product
    current_index = 0
    results = []
    while current_index < len(circular_list):
        current_number = circular_list[current_index]
        for sublist_length in range(current_index + 1):
            sublist = [circular_list[(current_index + k) % len(circular_list)] for k in range(sublist_length + 1)]
            if product(sublist) == 29:
                results.append(sublist)
        current_index += 1
        if will_wrap(current_index, len(circular_list)):
            break
    return results