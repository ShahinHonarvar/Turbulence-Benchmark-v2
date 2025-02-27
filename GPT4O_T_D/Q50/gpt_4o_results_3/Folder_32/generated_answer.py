from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if is_anagram(normalized_strings[i], normalized_strings[j]):
                count += 1
                if count >= 194:
                    return True
    return False