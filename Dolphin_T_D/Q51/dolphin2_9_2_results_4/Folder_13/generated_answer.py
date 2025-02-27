def if_contains_anagrams(lis):
    result = 0
    for i in range(len(lis)):
        for j in range(i + 1, len(lis)):
            str1 = lis[i].lower()
            str2 = lis[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
                result += 1
            if result > 54:
                return True
    return False