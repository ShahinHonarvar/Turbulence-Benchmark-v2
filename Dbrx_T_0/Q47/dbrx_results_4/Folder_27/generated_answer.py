def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(13, 100):
        for length in range(26, 30):
            if i + length <= len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes