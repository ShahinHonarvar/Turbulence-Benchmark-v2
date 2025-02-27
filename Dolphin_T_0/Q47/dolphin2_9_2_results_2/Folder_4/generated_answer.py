def palindromes_of_specific_lengths(s):
    s = s[11:92].lower()
    palindromes_set = set()
    for length in range(17, 67):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes_set.add(s[i:i + length])
    return palindromes_set