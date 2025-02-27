import itertools
  from collections import Counter

def if_contains_anagrams(list_of_strings):
    lowercase_list = [string.lower() for string in list_of_strings]
    anagram_count = 0
    for i in range(len(lowercase_list) - 1):
        for j in range(i + 1, len(lowercase_list)):
            if len(lowercase_list[i]) >= 3 and len(lowercase_list[j]) >= 3 and (Counter(lowercase_list[i]) == Counter(lowercase_list[j])):
                anagram_count += 1
    if anagram_count <= 64:
        return True
    else:
        return False