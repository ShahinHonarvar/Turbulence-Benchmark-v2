import string

def if_contains_anagrams(word_list):
    anagram_dict = {}
    for word in word_list:
        word = word.lower()
        word = word.translate(str.maketrans('', '', string.punctuation))
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    count = sum([val for val in anagram_dict.values()])
    if count <= 10:
        return True
    else:
        return False