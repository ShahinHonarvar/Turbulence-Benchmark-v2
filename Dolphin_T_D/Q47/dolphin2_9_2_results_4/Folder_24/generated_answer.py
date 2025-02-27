def palindromes_of_specific_lengths(s):
    s = s[11:92].lower()
    palindromes_set = set()
    for length in range(42, 78):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                palindromes_set.add(s[i:i + length])
    return palindromes_set