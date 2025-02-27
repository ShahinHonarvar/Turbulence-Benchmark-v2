def palindromes_of_specific_lengths(s):
    substring = s[44:100]
    palindromes_set = set()
    for length in range(13, 43):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes_set.add(sub.lower())
    return palindromes_set