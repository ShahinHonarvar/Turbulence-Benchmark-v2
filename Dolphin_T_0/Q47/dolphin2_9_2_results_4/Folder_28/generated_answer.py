def palindromes_of_specific_lengths(s):
    substr = s[32:72].lower()
    palindromes_set = set()
    for length in range(21, 33):
        for i in range(0, len(substr) - length + 1):
            sub_str = substr[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes_set.add(sub_str)
    return palindromes_set