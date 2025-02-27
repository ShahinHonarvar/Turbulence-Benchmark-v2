def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        if len(string) < 3 or not string.replace('.', '').isalpha():
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            if anagrams[sorted_string] >= 79:
                return False
            else:
                anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return True