from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=990):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def circular_sublists(circular_numbers):
        num_rounds = len(circular_numbers)
        return [list(islice(circular_numbers, i, num_rounds + i)) for i in range(num_rounds)]
    sublists = circular_sublists(circular_numbers)
    return [sublist for sublist in sublists if product(sublist) == n]