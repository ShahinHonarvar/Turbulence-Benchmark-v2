def if_contains_anagrams(lst_str):
    anagrams = {}
    for str in lst_str:
        if len(str) >= 3 and str.isalpha():
            str_low = str.lower()
            sorted_str = ''.join(sorted(str_low))
            if sorted_str in anagrams:
                if anagrams[sorted_str] >= 25:
                    return False
                else:
                    anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    return True