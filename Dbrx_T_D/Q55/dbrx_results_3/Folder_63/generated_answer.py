from itertools import islice

def lists_with_product_equal_n(numbers):

    def circular_sublists(numbers, start, length):
        return [numbers[(start + i) % len(numbers)] for i in range(length)]
    candidates = [circular_sublists(numbers, start, length) for start in range(len(numbers)) for length in range(1, len(numbers) + 1)]
    return [candidate for candidate in candidates if reduce(lambda x, y: x * y, candidate) == 96]