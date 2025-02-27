def palindromes_of_specific_lengths(s):
    substring = s[10:75]
    pal = set()
    for length in range(6, 9):
        for i in range(len(substring)):
            temp = substring[i:i + length]
            if temp == temp[::-1] and temp.isalpha() and (temp.lower() == temp):
                pal.add(temp)
    return pal