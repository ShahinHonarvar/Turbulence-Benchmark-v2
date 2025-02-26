def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for i in range(11, 98):
        for length in range(29, 63):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes