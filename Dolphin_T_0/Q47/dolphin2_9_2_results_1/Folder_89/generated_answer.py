def palindromes_of_specific_lengths(s):
    s = s[17:89]
    set_of_palindromes = set()
    for i in range(len(s)):
        for length in [12, 13, 14]:
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    set_of_palindromes.add(substring.lower())
    return set_of_palindromes