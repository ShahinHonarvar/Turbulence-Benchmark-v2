import collections

def return_n_greatest_chars(string):
    char_dict = collections.Counter(string)
    sorted_characters = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)[:47]
    return [char for char, count in sorted_characters]