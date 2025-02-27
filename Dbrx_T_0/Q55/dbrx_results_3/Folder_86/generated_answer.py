from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n):

    def sublists_with_product_equal_n(numbers, n, start, end):
        if start == end:
            return [numbers[start:start + 1]] if n == numbers[start] else []
        result = []
        for i in range(start, end):
            sub = numbers[start:i + 1]
            product = sub[0]
            for j in sub[1:]:
                product *= j
            if product == n:
                result.append(sub)
            elif product < n:
                result.extend(sublists_with_product_equal_n(numbers, n, i + 1, end))
        return result
    return sublists_with_product_equal_n(list(cycle(numbers)), n, 0, len(numbers))