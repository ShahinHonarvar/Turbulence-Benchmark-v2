from collections import Counter

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        if len(list_of_strings[i]) >= 3:
            key = ''.join(sorted(Counter(list_of_strings[i]).elements()))
            for j in range(i + 1, len(list_of_strings)):
                if len(list_of_strings[j]) >= 3:
                    if ''.join(sorted(Counter(list_of_strings[j]).elements())) == key:
                        count += 1
    return count <= 41