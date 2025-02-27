def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[17:73]
    for i in range(len(substring)):
        for j in range(i + 50, i + 52):
            if j > len(substring):
                break
            sub = substring[i:j]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes