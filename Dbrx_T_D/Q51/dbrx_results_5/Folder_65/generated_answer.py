import string

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower().translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).translate(str.maketrans('', '', string.whitespace))
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
                if anagrams[sorted_s] > 72:
                    return True
            else:
                anagrams[sorted_s] = 1
    return False