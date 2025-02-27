def palindromes_of_specific_lengths(s):
    substring = s[26:85]
    palindromes = set()
    for i in range(30, 47):
        for j in range(len(substring) - i + 1):
            temp = substring[j:j + i]
            if temp == temp[::-1] and temp.isalpha():
                palindromes.add(temp.lower())
    return palindromes