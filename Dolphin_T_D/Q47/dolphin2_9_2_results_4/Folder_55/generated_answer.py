def palindromes_of_specific_lengths(s):
    s = s[10:76]
    palindromes_set = set()
    for length in range(10, 21):
        for i in range(len(s)):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                palindromes_set.add(s[i:i + length])
    return palindromes_set