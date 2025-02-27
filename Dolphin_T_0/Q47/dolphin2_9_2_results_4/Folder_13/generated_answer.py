def palindromes_of_specific_lengths(s):
    s = s[13:96]
    palindromes = set()
    for length in range(57, 61):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() or not char.isalpha() for char in substring.lower())):
                substring = ''.join(filter(str.isalpha, substring.lower()))
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes