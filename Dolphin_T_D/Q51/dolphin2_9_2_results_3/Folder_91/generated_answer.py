def if_contains_anagrams(string_list):
    counter = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if are_anagrams(string_list[i], string_list[j]):
                counter += 1
    return counter <= 88

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    for char in str1:
        if char not in str2:
            return False
    return True