def palindromes_of_specific_lengths(s):
    s = s[23:83]
    result = set()
    for i in range(len(s)):
        if i + 34 > len(s):
            break
        temp = ''
        for j in range(i, i + 34):
            if temp.lower() == temp.lower()[::-1] and len(temp) >= 32:
                result.add(temp)
            if j - i < 31:
                temp += s[j]
    return result