def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes