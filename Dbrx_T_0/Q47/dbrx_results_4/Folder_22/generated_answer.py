def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(100, 201):
        for length in range(5, 11):
            if i + length <= len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes