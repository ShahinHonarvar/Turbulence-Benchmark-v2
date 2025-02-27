def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[31:75]
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes