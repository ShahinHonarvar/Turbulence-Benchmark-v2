def palindromes_of_specific_lengths(s):
    substring = s[155:284]
    palindromes = set()
    for i in range(104, 121):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes