def palindromes_of_specific_lengths(s):

    def is_palindrome(sub_str):
        return sub_str == sub_str[::-1]
    substring = s[18:99]
    palindromes = set()
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            sub_str = substring[start:start + length]
            if sub_str.isalpha() and is_palindrome(sub_str.lower()):
                palindromes.add(sub_str)
    return palindromes