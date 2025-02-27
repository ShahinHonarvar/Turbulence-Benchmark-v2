from collections import OrderedDict

def remove_repeat_chars(s: str) -> str:
    substr = s[46:91]
    ord_dict = OrderedDict()
    for char in substr:
        if char not in ord_dict:
            ord_dict[char] = [substr.index(char)]
        else:
            ord_dict[char].append(substr.index(char))
    for occurrences in ord_dict.values():
        if len(occurrences) > 1:
            for i in range(len(selford_dict[char])):
                if i != occurrences[i]:
                    s = s[:occurrences[i]] + s[occurrences[i] + 1:]
    return s