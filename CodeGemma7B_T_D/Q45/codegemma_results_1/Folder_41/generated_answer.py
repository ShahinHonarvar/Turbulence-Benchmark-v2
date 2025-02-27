from string import ascii_lowercase

def palindromes_between_indices(txt):
    low_txt = txt.lower()
    results = set()
    for start in range(len(low_txt) - 2):
        for end in range(start + 2, len(low_txt) + 1):
            word = low_txt[slice(start, end)]
            if word == word[::-1] and all((c in ascii_lowercase for c in word)):
                results.add(word)
    return results