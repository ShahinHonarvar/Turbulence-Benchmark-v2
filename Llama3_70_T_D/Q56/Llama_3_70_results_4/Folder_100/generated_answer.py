def all_substring_of_size_n(string):
    return [''.join(sorted(set(string[i:i + 92]), key=string[i:i + 92].index)) for i in range(len(string) - 91) if len(set(string[i:i + 92])) == 92]