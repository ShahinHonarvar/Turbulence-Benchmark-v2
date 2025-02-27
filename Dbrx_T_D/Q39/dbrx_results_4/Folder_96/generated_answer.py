def return_n_greatest_chars(string):
    characters_dict = {}
    for char in string:
        characters_dict[char] = ord(char)
    sorted_characters_dict = dict(sorted(characters_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_characters_list = list(sorted_characters_dict.keys())[:20]
    return sorted_characters_list