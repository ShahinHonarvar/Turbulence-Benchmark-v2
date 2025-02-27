def if_contains_anagrams(string_list):

    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            str1 = ''.join(filter(str.isalpha, string_list[i]))
            str2 = ''.join(filter(str.isalpha, string_list[j]))
            if len(str1) >= 3 and len(str2) >= 3 and are_anagrams(str1, str2):
                count += 1
        if count > 2:
            return False
    return True