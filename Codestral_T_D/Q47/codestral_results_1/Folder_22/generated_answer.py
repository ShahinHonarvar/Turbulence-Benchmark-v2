def palindromes_of_specific_lengths(s):
    substring = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes