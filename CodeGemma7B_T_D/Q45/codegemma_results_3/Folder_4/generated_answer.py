import itertools

def palindromes_between_indices(string):
    ascii_lowercase = list(itertools.chain(*[list(x) for x in iter(ord, ord('a'), ord('z') + 1)]))
    all_options = []
    for sublist in itertools.combinations_with_replacement(ascii_lowercase, 7):
        joined = ''.join(sublist)
        if joined[0] >= ord('a') and joined[0] <= ord('z'):
            all_options.append(joined)
    return set(all_options)