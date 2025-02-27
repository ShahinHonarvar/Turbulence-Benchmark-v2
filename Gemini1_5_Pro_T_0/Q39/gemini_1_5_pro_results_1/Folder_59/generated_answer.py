def return_n_greatest_chars(text_):
    sorted_characters = sorted(text_, reverse=True)
    return sorted_characters[:13]