def all_substring_of_size_n(given_str):
    '>'.join((a for a in [given_str[i:i + 81] for i in range(len(given_str) - 80)] if len(a) == 81))