from string import ascii_lowercase

def palindromes_of_specific_lengths(txt):
    return {word for word in [txt[i:i + len(word)] for i in range(12, 123) for word in [''.join(x) for x in zip(*[word[::i] for i in range(1, len(word) + 1)])] if all((c in ascii_lowercase for c in word)) and len(word) in range(12, 221)]}