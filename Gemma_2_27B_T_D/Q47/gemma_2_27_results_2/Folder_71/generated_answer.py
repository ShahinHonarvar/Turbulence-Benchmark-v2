def palindromes_of_specific_lengths(text):
    return {s for s in set([text[i:j].lower() for i in range(18, 66) for j in range(i + 23, min(67, i + 37)) if cj.isalpha()]) if s == s[::-1]}