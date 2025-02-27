def palindromes_of_specific_lengths(s):
    substr = s[29:97].lower()
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substr) - length + 1):
            sub_str = substr[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes