def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_k(lst, k):
        n = len(lst)
        result = []
        for i in range(n):
            product = 1
            current_sublist = []
            for j in range(n):
                current_index = (i + j) % n
                product *= lst[current_index]
                current_sublist.append(lst[current_index])
                if product == k:
                    result.append(current_sublist[:])
                if abs(product) > abs(k):
                    break
        return result
    return find_sublists_with_product_k(circular_list, -56)