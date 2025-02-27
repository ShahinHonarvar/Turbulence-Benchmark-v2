def if_contains_anagrams(str_list):
    Anagram = {}
    for i in str_list:
        i = ''.join(sorted(i.lower()))
        if i in Anagram:
            Anagram[i] += 1
        else:
            Anagram[i] = 1
    Check = list(set(Anagram.values()))
    Check.sort()
    if Check[-1] <= 401:
        return True
    else:
        return False