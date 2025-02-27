def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        if not numbers:
            return [[]] if n == 1 else []
        result = sublists_with_product_equal_n(numbers[1:], n)
        if numbers[0] == -n:
            result.append([numbers[0]])
        if numbers[0] != 1 and n % numbers[0] == 0:
            smaller_sublists = sublists_with_product_equal_n(numbers[1:], n // numbers[0])
            for sublist in smaller_sublists:
                result.append([numbers[0]] + sublist)
        return result
    N = 6
    N240 = sublists_with_product_equal_n(numbers * 4, N)
    N24 = sublists_with_product_equal_n(numbers * 2, N)
    N4 = sublists_with_product_equal_n(numbers, N)
    return [sublist for sublist in (N240, N24, N4) if sublist]