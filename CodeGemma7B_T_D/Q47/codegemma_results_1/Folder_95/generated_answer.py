def palindromes_of_specific_lengths(str1):
    str1 = str1.lower()
    temp = []
    for i in range(12, 57):
        for j in range(i):
            s = str1[j:i + 1]
            if len(s) >= 20 and len(s) <= 21 and (s == s[::-1]):
                temp.append(s)
    return set(temp)