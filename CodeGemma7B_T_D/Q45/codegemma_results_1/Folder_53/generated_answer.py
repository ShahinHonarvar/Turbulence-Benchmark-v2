def palindromes_between_indices(text):
    range = text[4:9].lower().replace(' ', '')
    if len(range) > 9:
        return set()
    for p in itertools.permutations(range, len(range)):
        result = ''.join(p)
        if len(result) >= 6 and result == result[::-1]:
            yield result