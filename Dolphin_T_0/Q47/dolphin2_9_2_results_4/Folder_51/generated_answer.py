def palindromes_of_specific_lengths(s):
    substring = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes