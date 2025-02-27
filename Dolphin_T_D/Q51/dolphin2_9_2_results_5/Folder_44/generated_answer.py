def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = ''
            str2 = ''
            for char in lst[i]:
                if char.isalpha():
                    str1 += char.lower()
            for char in lst[j]:
                if char.isalpha():
                    str2 += char.lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3 and (len(str2) >= 3):
                anagrams_count += 1
    if anagrams_count <= 75:
        return True
    else:
        return False