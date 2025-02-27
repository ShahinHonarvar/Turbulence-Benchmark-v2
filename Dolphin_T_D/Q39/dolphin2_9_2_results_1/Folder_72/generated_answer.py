def return_n_greatest_chars(string):
    characters = sorted([char for char in string], reverse=True)
    return characters[:37]