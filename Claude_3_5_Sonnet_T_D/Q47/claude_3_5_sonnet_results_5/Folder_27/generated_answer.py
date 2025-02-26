def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[13:100]
    for i in range(len(substring)):
        for j in range(i + 26, min(i + 30, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 26 <= len(cleaned_palindrome) <= 29:
                result.add(cleaned_palindrome)
    return result