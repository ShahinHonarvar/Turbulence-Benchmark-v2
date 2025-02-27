import string

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower())).translate(str.maketrans('', '', string.punctuation))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                anagram_pairs += 1
        if anagram_pairs > 69:
            return False
    return True