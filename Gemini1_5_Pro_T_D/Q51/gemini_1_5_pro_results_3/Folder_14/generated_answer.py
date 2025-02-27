from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(list)
    for word in list_of_strings:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        if n >= 2:
            count += n * (n - 1) // 2
    if count <= 474:
        return True
    else:
        return False