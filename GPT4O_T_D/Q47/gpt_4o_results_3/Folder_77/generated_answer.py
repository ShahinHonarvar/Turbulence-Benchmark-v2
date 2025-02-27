def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_letters(sub):
        return ''.join(filter(str.isalpha, sub))
    s = s.lower()
    specified_substring = s[103:277]
    palindromes = set()
    for length in range(100, 170):
        for start in range(0, len(specified_substring) - length + 1):
            substring = specified_substring[start:start + length]
            filtered_substring = extract_letters(substring)
            if len(filtered_substring) == length and is_palindrome(filtered_substring):
                palindromes.add(filtered_substring)
    return palindromes