def palindromes_of_specific_lengths(text):
    return {word for word in set(filter(lambda x: x.isalpha() and len(x) >= 40 and (len(x) <= 47) and (x.lower() == x[::-1].lower()), text[45:99]))}