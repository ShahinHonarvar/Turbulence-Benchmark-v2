def if_contains_anagrams(str_list):
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i]
            str2 = str_list[j]
            str1 = ''.join(sorted([char.lower() for char in str1 if char.isalpha()]))
            str2 = ''.join(sorted([char.lower() for char in str2 if char.isalpha()]))
            if str1 == str2 and len(str1) >= 3:
                pairs += 1
    return pairs <= 93