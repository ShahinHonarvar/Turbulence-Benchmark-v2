def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            sub_str = s[i:i + length]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes