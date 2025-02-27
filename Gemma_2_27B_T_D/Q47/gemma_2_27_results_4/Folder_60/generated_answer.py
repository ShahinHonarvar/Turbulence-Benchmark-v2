def palindromes_of_specific_lengths(text):
    return {word for word in set([''.join((c for c in text[23:83].lower() if c.isalpha())).split()]) if len(word) in range(32, 35) and word == word[::-1]}