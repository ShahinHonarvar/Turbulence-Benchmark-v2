def palindromes_of_specific_lengths(text):
    return {x for x in set([i for i in text[0:11] if i.isascii() and i.isalpha() and (len(i) in range(3, 6)) and (i.lower() == i[::-1].lower())])}