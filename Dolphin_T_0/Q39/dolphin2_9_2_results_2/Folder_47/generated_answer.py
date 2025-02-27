def return_n_greatest_chars(s):
    characters = [c for c in s]
    characters.sort(reverse=True)
    return characters[:21]