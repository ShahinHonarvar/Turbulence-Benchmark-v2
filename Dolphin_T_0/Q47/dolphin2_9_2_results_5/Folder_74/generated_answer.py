def palindromes_of_specific_lengths(s):
    substring = s[30:85]
    palindromes = set()
    for i in range(12, 21):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub.lower() == sub[::-1].lower():
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes