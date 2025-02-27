import string

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    words = [''.join(sorted(word)) for word in words if len(set(word)) >= 3]
    anagrams = [word for word in words if word[0] not in string.punctuation]
    anagram_set = set(anagrams)
    return len(anagrams) - len(anagram_set) <= 26