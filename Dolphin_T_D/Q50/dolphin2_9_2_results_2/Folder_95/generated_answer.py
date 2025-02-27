def if_contains_anagrams(lst):
    result = 0
    for i in range(len(lst)):
        temp = ''
        for j in lst[i]:
            if j.isalpha():
                temp += j.lower()
        if len(temp) >= 3:
            for k in range(i + 1, len(lst)):
                temp2 = ''
                for j in lst[k]:
                    if j.isalpha():
                        temp2 += j.lower()
                if len(temp2) >= 3 and sorted(temp) == sorted(temp2):
                    result += 1
    return result >= 93