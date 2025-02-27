def palindromes_of_specific_lengths(s):
    subset = s[124:284]
    palindromes = set()
    for i in range(length):
        sub = subset[i:i + length]
        if sub == sub[::-1] and sub.isalpha():
            palindromes.add(sub.lower())
    return palindromes