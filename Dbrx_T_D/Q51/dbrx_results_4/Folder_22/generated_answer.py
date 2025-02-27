import string

def if_contains_anagrams(lst):
    anagrams = set()
    count = 0
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3 and all((c in string.ascii_lowercase for c in sorted_word)):
            if sorted_word in anagrams:
                count += 1
                if count > 14:
                    return False
            else:
                anagrams.add(sorted_word)
    return True