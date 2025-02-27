import string

def if_contains_anagrams(string_list):
    anagrams = set()
    for s in string_list:
        s = s.lower()
        if len(s) < 3 or s.translate(str.maketrans('', '', string.punctuation)) != s:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams.add(sorted_s)
    return len(anagrams) >= 94