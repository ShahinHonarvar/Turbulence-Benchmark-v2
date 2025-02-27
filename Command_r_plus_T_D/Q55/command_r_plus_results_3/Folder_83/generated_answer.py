def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, product):
        subarrays = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                if product(array[i:j + 1]) == product:
                    subarrays.append(array[i:j + 1])
        return subarrays
    product_list = find_subarrays(circular_list, -57)
    circular_list.append(circular_list[0])
    product_list.extend(find_subarrays(circular_list, -57))
    return product_list