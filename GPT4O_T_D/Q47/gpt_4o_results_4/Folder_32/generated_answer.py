def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[16:78]
    palindromes = set()
    for length in range(43, 48):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            filtered_sub = ''.join(filter(str.isalpha, substring)).lower()
            if len(filtered_sub) == length and is_palindrome(filtered_sub):
                palindromes.add(substring)
    return palindromes