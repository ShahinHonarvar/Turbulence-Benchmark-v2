def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        substr = s[i:i + 3]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    for i in range(len(s) - 3):
        substr = s[i:i + 4]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes