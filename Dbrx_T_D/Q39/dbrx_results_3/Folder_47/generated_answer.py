def return_n_greatest_chars(string_argument):
    distinct_characters = list(set(string_argument))
    sorted_characters = sorted(distinct_characters, reverse=True)
    return sorted_characters[:21]