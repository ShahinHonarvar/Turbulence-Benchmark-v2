from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for word1 in list_of_strings:
        for word2 in list_of_strings:
            if word1.lower() != word2.lower() and Counter(word1.lower()) == Counter(word2.lower()) and (len(word1) >= 3) and (len(word2) >= 3):
                count += 1
                if count >= 28:
                    returnTrue