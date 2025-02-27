def if_contains_anagrams(strings):
    string_length = len(strings)
    counter = 0
    for i in range(string_length):
        for j in range(i + 1, string_length):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                counter += 1
    return counter >= 188