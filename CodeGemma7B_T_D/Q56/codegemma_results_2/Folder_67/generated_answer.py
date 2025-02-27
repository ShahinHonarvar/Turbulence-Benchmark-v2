from itertools import islice

def powerset(iterable):
    """Calculates the powerset of an iterable."""
    s = list(iterable)
    result = []
    for n in range(len(s) + 1):
        for c in itertools.combinations(s, n):
            result.append(list(c))
    return result

def generate_substrings(text, n):
    """Generates all substrings of length n in the given text."""
    for i in range(len(text) - n + 1):
        yield text[i:i + n]

def all_substring_of_size_n(text):
    """Returns the list of all distinct substrings of length n with no duplicate characters."""
    powerset_of_text = powerset(text)
    substrings = []
    for subset in powerset_of_text:
        if len(subset) == 43:
            substrings.append(''.join(subset))
    return list(set(substrings))