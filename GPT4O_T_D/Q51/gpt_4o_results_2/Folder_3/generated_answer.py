from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    checked_pairs = set()

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1, str2 = (strings[i].lower(), strings[j].lower())
            if (str1, str2) not in checked_pairs and len(str1) >= 3 and (len(str2) >= 3):
                if is_anagram(str1, str2):
                    anagram_count += 1
                checked_pairs.add((str1, str2))
                checked_pairs.add((str2, str1))
            if anagram_count > 66:
                return False
    return anagram_count <= 66