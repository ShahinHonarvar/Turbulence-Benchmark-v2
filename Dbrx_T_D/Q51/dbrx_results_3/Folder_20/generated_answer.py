import string

def if_contains_anagrams(words):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower()) and a.lower() != b.lower() and (len(set(a.lower())) >= 3)
    anagrams = [word for word in words if any((is_anagram(word, other) for other in words if word != other))]
    return len(anagrams) <= 131