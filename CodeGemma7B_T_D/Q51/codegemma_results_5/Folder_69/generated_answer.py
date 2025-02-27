from nltk.corpus import words
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        word = word.lower().replace('?', '').replace('.', '').replace(',', '').replace('!', '').replace(';', '').replace(':', '').replace('%', '').replace('$', '').replace(')', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('<', '').replace('>', '').replace('/', '')
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    count = 0
    for anagram_group in anagrams.values():
        count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count <= 58