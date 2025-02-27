def palindromes_of_specific_lengths(s):
    substring = s[40:95]
    palindrome_set = set()
    for length in range(45, 52):
        for i in range(length, len(substring) + 1):
            sub_str = substring[i - length:i]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindrome_set.add(sub_str)
    return palindrome_set