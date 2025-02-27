def lists_with_product_equal_n(lst):

    def generate_sublists(lst):
        n = len(lst)
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield lst[i:j]
    result = [sublist for sublist in generate_sublists(lst) if sublist and functools.reduce(lambda x, y: x * y, sublist) == 36]
    if not result:
        return []
    else:
        return result