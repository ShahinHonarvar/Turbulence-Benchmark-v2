def lists_with_product_equal_n(circular_list):

    def generate_sublists(lst, size):
        for i in range(len(lst)):
            sub = [lst[(i + j) % len(lst)] for j in range(size)]
            yield sub
    result = []
    n = len(circular_list)
    for size in range(1, n + 1):
        for sub in generate_sublists(circular_list, size):
            product = 1
            for num in sub:
                product *= num
            if product == 6:
                result.append(sub)
    return result