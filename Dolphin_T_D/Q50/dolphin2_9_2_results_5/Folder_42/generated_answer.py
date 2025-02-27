def if_contains_anagrams(list_ofstrings):
    count = 0
    for i in range(len(list_ofstrings) - 1):
        for j in range(i + 1, len(list_ofstrings)):
            if len(list_ofstrings[i]) >= 3 and len(list_ofstrings[j]) >= 3:
                if sorted(list_ofstrings[i].lower()) == sorted(list_ofstrings[j].lower()):
                    count += 1
    if count >= 233:
        return True
    else:
        return False