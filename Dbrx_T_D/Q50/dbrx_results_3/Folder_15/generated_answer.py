import string

def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower().translate(str.maketrans('', '', string.punctuation))))
    anagrams = {}
    for s in strings:
        sorted_s = sort_string(s)
        if len(sorted_s) >= 3:
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    return sum((count // 2 for count in anagrams.values())) >= 4