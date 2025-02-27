import collections
import string

def if_contains_anagrams(list_of_strings):
    maj_ana = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (str1.translate(str.maketrans('', '', string.punctuation)) != '') and (str2.translate(str.maketrans('', '', string.punctuation)) != ''):
                if collections.Counter(str1) == collections.Counter(str2):
                    maj_ana += 1
    if maj_ana > 39:
        return True
    else:
        return False