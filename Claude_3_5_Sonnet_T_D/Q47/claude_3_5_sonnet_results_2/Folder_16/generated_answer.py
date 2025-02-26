def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:87]
    lowercase_substring = substring.lower()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            potential_palindrome = lowercase_substring[i:i + length]
            cleaned_palindrome = ''.join((char for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and len(cleaned_palindrome) == length:
                result.add(substring[i:i + length])
    return result