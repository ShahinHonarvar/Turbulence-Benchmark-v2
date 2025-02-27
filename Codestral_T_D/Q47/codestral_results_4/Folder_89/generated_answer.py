def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[18:89].lower()
    for i in range(len(substring)):
        for j in range(12, 15):
            if i + j <= len(substring):
                sub = substring[i:i + j]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes