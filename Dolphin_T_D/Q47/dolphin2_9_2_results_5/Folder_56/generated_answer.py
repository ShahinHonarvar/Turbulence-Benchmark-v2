def palindromes_of_specific_lengths(s):
    s = s[1:10]
    palindromes = set()
    for i in range(3, 8):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((char.isalpha() for char in substring)):
                substring = substring.lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes