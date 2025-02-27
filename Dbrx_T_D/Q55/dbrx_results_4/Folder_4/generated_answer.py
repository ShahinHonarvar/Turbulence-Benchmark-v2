def lists_with_product_equal_n(numbers):

    def calculate_product(numbers):
        product = 1
        for number in numbers:
            product *= number
        return product

    def sublists_with_product_equal_n(numbers, n):
        sublists = []
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                sublist = numbers[i:j + 1]
                if calculate_product(sublist) == n:
                    sublists.append(sublist)
        return sublists
    result = sublists_with_product_equal_n(numbers, 91)
    circular_numbers = numbers + [numbers[0]]
    circular_result = sublists_with_product_equal_n(circular_numbers, 91)
    return [sublist for sublist in circular_result if sublist not in result]