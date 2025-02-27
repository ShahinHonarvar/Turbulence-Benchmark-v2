def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            for i in range(len(strings)):
                if i != strings.index(string):
                    if sorted(string.lower()) == sorted(strings[i].lower()):
                        anagram_count += 1
    if anagram_count >= 57:
        return True
    else:
        return False