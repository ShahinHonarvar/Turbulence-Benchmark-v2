def palindromes_of_specific_lengths(text):
    return {p for p in set([text[i:j + 1].lower() for i in range(17, 73) for j in range(i, 72)]) if len(p) in range(50, 52) and p == p[::-1] and p.isalpha()}