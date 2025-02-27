def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    valid_palindromes = set()
    substring_interest = s[13:96]
    cleaned_substring = ''.join(filter(str.isalpha, substring_interest))
    cleaned_substring_lower = cleaned_substring.lower()
    for length in range(57, 61):
        for i in range(len(cleaned_substring_lower) - length + 1):
            candidate = cleaned_substring_lower[i:i + length]
            if is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes