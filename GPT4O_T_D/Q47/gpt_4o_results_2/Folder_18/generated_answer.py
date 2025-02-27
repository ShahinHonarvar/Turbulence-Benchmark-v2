def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[11:84]
    palindromes = set()
    normalized_s = ''.join(filter(str.isalpha, s)).lower()
    for start in range(len(normalized_s)):
        for length in range(13, 67):
            end = start + length
            if end > len(normalized_s):
                break
            substring = normalized_s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes