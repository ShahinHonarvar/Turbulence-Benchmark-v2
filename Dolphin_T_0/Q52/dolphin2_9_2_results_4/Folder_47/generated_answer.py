def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if len(substring) == 34:
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
        if i < len(s) - 1:
            j = i + 1
            while j < len(s):
                substring = s[i:j + 1]
                if len(substring) == 34:
                    if substring.lower() == substring.lower()[::-1]:
                        palindromes.add(substring)
                j += 1
    return palindromes