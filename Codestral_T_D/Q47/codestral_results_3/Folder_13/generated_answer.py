def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    palindromes = set()
    for i in range(len(s) - 56):
        for j in range(57, 61):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    if substring.isalpha():
                        palindromes.add(substring)
    return palindromes