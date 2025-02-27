def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 97):
        for length in range(45, 53):
            if i + length - 1 < len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes