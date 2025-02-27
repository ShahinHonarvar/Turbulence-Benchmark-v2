import string

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for s in list_of_strings:
        s = s.lower()
        s = ''.join(sorted(s))
        if len(s) >= 3 and s in english_letters:
            if s in anagrams:
                anagrams[s] += 1
                if anagrams[s] == 2:
                    count += 1
                    if count > 34:
                        return False
            else:
                anagrams[s] = 1
    return True