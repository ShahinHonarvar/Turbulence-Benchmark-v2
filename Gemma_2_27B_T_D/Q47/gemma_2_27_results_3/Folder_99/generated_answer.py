def palindromes_of_specific_lengths(text):
    return {p for p in set([text[i:i + l].lower() for i in range(127, 289 - l + 1) for l in range(119, 142)]) if p == p[::-1] and p.isalpha()}