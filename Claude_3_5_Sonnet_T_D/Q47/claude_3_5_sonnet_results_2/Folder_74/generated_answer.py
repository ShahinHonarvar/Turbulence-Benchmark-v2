def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[30:85]
    lowercase_substring = substring.lower()
    for i in range(len(substring)):
        for length in range(12, 21):
            if i + length > len(substring):
                break
            potential_palindrome = lowercase_substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                result.add(substring[i:i + length])
    return result