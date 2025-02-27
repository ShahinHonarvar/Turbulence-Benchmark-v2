def lists_with_product_equal_n(circular_list):

    def find_product_sublist(lst):
        n = len(lst)
        results = []
        for i in range(n):
            product = 1
            for j in range(n):
                product *= lst[(i + j) % n]
                if product == 37:
                    sub_list = [lst[(i + k) % n] for k in range(j + 1)]
                    results.append(sub_list)
                if product == 0 or product > 37:
                    break
        return results
    return find_product_sublist(circular_list)