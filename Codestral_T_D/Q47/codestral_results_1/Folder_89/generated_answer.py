def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[18:89]
    for i in range(len(substring)):
        for j in range(i + 12, i + 15):
            if j <= len(substring) and substring[i:j].isalpha():
                word = substring[i:j].lower()
                if word == word[::-1]:
                    palindromes.add(substring[i:j])
    return palindromes