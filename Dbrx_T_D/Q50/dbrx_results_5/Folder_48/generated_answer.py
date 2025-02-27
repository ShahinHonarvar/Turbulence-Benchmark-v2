import string

def if_contains_anagrams(word_list):
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            word1 = word_list[i].lower().translate(str.maketrans('', '', string.punctuation))
            word2 = word_list[j].lower().translate(str.maketrans('', '', string.punctuation))
            if sorted(word1) == sorted(word2) and len(word1) >= 3:
                anagram_pairs += 1
        if anagram_pairs >= 219:
            return True
    return False