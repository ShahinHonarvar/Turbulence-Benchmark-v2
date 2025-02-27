from collections import Counter
import itertools

def if_contains_anagrams(words):
    English_Letters = 'abcdefghijklmnopqrstuvwxyz'
    Anagram_Pairs = 0
    for i in range(len(words) - 1):
        word1 = words[i].lower()
        if len(word1) >= 3:
            for j in range(i + 1, len(words)):
                word2 = words[j].lower()
                if len(word2) >= 3:
                    if sorted(word1) == sorted(word2):
                        word1_set = set(word1)
                        if word1_set.issubset(word2) and len(word2.replace(''.join(word1_set), '')) == 0:
                            Anagram_Pairs += 1
                        else:
                            Anagram_Pairs += 1
    if Anagram_Pairs <= 366:
        return True
    else:
        return False