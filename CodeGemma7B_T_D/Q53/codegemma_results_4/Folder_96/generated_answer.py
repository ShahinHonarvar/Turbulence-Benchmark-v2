from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    result = set()
    char_map = defaultdict(list)
    for i, char in enumerate(string.lower()):
        char_map[char].append(i)
    for i, char in enumerate(string.lower()):
        for j in range(i + 1, len(string)):
            if string[i:j + 1][::-1] in char_map[char]:
                result.add(string[i:j + 1])
    return result