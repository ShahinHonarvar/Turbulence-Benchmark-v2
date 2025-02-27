from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) >= 3:
            string = string.lower()
            sorted_string = ''.join(sorted(string))
            count += count_dict.get(sorted_string, 0)
            if count > 289:
                return False
    return True