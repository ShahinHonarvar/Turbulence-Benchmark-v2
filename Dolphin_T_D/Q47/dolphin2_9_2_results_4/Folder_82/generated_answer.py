def palindromes_of_specific_lengths(s):
    s = s[3:301]
    result = set()
    for i in range(len(s) - 29):
        temp = ''.join((e for e in s[i:i + 30] if e.isalpha()))
        for length in range(30, len(temp) + 1):
            temp = temp[i:i + length]
            if temp == temp[::-1]:
                result.add(temp)
    return result