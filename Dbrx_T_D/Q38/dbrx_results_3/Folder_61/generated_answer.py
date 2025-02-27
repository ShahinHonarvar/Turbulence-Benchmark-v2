def find_subset_of_length_n(s, n=8):
    if n != 8:
        return 'The function is designed to find subsets of size 8 only.'
    return len(list(iterate_subsets(s, n)))

def iterate_subsets(s, n):
    if n == 0:
        yield set()
        return
    for subset in iterate_subsets(s, n - 1):
        for element in s - subset:
            yield (subset | {element})
        yield subset