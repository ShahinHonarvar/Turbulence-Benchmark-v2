def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[155:284].lower()
    for i in range(len(substring)):
        for j in range(i + 104, i + 121):
            if j > len(substring):
                break
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes