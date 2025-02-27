def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            x = sorted(list_of_strings[i].lower().replace(' ', ''))
            y = sorted(list_of_strings[j].lower().replace(' ', ''))
            if len(x) >= 3 and len(y) >= 3 and set('abcdefghijklmnopqrstuvwxyz').issuperset(set(x + y)):
                if x == y:
                    count += 1
    return count <= 98