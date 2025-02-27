def palindromes_of_specific_lengths(s):
    substring = s[23:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes