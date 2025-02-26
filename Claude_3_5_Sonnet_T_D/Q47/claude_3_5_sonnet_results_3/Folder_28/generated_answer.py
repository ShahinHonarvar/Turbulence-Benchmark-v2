def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[32:72]
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 33, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 21 <= len(cleaned_palindrome) <= 32:
                result.add(potential_palindrome)
    return result