from collections import defaultdict

def all_substring_of_size_n(string):
    substring_length = 26
    result = []
    unique_characters = set()
    for i in range(len(string)):
        for j in range(i + substring_length - 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) == substring_length and len(set(substring)) == substring_length:
                unique_characters.add(substring)
    result.extend(unique_characters)
    return result