def palindromes_of_specific_lengths(text):
    return {word for word in set(filter(lambda x: x.isalpha() and 26 <= len(x) <= 33 and (x.lower() == x[::-1].lower()), text[65:100]))}