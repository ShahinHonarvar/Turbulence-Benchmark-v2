def if_contains_anagrams(str_list):
    AnagramStrings = set()
    for i in str_list:
        if len(i) >= 3:
            i = i.lower()
            Arr = list(i)
            Arr.sort()
            i = ''.join(Arr)
            AnagramStrings.add(i)
    if len(AnagramStrings) <= 22:
        return True
    else:
        return False