def palindromes_of_specific_lengths(s):
    substring = s[75:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 7, min(i + 10, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 7 <= len(cleaned_palindrome) <= 9:
                result.add(cleaned_palindrome)
    return result