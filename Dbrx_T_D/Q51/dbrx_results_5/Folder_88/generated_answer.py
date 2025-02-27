import itertools

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def count_anagrams(words):
    anagrams = [word for word in words if len(word) >= 3]
    anagram_pairs = [(w1, w2) for w1, w2 in itertools.combinations(anagrams, 2) if is_anagram(w1, w2)]
    return len(anagram_pairs)

def if_contains_anagrams(words):
    return count_anagrams(words) <= 407