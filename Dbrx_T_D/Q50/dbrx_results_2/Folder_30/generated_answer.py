import string

def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_s in anagrams and anagrams[sorted_s] == s:
                if anagrams[sorted_s] in {''.join(sorted(anagrams[sorted_s].lower()))}:
                    anagrams[sorted_s] = True
                else:
                    anagrams[sorted_s] = False
            if sorted_s not in anagrams:
                anagrams[sorted_s] = s
    count = 0
    for v in anagrams.values():
        if v is True:
            count += 1
    if count >= 78:
        return True
    else:
        return False