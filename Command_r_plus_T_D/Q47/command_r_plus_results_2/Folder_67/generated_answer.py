def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_str = s[64:100]
    palindromes = set()
    for length in range(26, 34):
        for i in range(len(sub_str) - length + 1):
            substring = sub_str[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes