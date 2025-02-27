def if_contains_anagrams(strings):
    count = 0
    for string in strings:
        if len(string) >= 3:
            for i in range(len(strings)):
                if len(strings[i]) >= 3 and sorted(strings[i].lower()) == sorted(string.lower()) and (i != strings.index(string)):
                    count += 1
                    strings[i] = ''
                    break
        if count == 5:
            return True
    return False