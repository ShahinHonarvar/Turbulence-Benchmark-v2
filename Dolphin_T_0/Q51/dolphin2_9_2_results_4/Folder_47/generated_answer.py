from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    checked = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in checked:
            checked.add(sorted_string)
            count += 1
        if count > 366:
            return False
    return True