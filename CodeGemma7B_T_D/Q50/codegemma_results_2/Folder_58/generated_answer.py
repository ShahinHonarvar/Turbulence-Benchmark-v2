def if_contains_anagrams(strings):
    strings.sort(key=len)
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i].lower() == strings[j].lower():
                count += 1
                if count >= 411:
                    return True
    return False