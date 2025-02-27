from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    def clean_string(s):
        return ''.join([c.lower() for c in s if c.isalpha()])
    count = 0
    checked = set()
    for i, word1 in enumerate(lst):
        word1_clean = clean_string(word1)
        if len(word1_clean) < 3:
            continue
        for j, word2 in enumerate(lst):
            if i != j and (i, j) not in checked and ((j, i) not in checked):
                word2_clean = clean_string(word2)
                if len(word2_clean) >= 3 and is_anagram(word1_clean, word2_clean):
                    count += 1
                    checked.add((i, j))
                    if count > 26:
                        return False
    return True