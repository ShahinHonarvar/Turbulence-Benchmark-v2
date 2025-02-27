from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            for i in range(len(anagram_dict[key])):
                for j in range(i + 1, len(anagram_dict[key])):
                    if anagram_dict[key][i].lower() != anagram_dict[key][j].lower():
                        return True
    return False