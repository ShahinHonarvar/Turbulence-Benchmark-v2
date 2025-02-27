def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    return str1_sorted == str2_sorted

def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
    if count >= 73:
        return True
    else:
        return False