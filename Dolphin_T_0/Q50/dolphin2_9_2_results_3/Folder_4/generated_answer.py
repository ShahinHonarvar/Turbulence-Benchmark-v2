from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) >= 3:
            for other_string in strings:
                if other_string != string and len(other_string) >= 3:
                    if Counter(string.lower()) == Counter(other_string.lower()):
                        count += 1
    return count >= 42