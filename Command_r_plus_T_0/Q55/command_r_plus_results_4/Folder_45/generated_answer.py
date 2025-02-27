def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == -5:
                    subarrays.append(arr[i:j + 1])
        return subarrays
    product_func = lambda x: -5 if -5 in [(prod := (lambda y: y[0] if len(y) == 1 else prod(y[1:]) * y[0])(x))] else prod
    sublists = find_subarrays(circular_list, product_func)
    sublists.extend(find_subarrays(circular_list[1:] + [circular_list[0]], product_func))
    return sublists