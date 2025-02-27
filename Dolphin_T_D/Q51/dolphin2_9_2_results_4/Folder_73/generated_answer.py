from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        for other_string in strings:
            if string != other_string and len(string) >= 3 and (len(other_string) >= 3) and (Counter(string.lower()) == Counter(other_string.lower())):
                count += 1
    return count <= 279