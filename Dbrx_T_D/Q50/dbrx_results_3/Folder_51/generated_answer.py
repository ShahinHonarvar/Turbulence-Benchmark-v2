import string

def if_contains_anagrams(string_list):
    anagram_count = 0
    for word in string_list:
        word = word.lower().translate(str.maketrans('', '', string.punctuation))
        if len(word) >= 3 and sorted(word) in [sorted(anagram) for anagram in string_list]:
            anagram_count += 1
    return anagram_count >= 39