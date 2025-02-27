def all_substring_of_size_n(string):
    return [substr for substr in [string[i:i + 33] for i in range(len(string) - 32)] if len(set(substr)) == 33]