def palindromes_of_specific_lengths(s):
    sub_str = s[1:8]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(sub_str) - length + 1):
            sub_sub_str = sub_str[i:i + length]
            if sub_sub_str == sub_sub_str[::-1] and sub_sub_str.isalpha():
                palindromes.add(sub_sub_str.lower())
    return palindromes