def if_contains_anagrams(strings_list):
    anagrams_count = 0
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    for string1 in strings_list:
        for string2 in strings_list:
            if string1 == string2:
                continue
            if len(string1) >= 3 and len(string2) >= 3 and all((letter in english_letters for letter in (string1, string2))) and (frozenset(string1.lower()) == frozenset(string2.lower())):
                anagrams_count += 1
    return anagrams_count <= 44